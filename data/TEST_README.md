# 测试数据说明

本目录下的测试文件用于验证「大模型生成文本检测」方案的推理与评测链路，
格式与 `scripts/preprocess.py` 产物完全一致，可直接喂给 `predict.py` 与 `eval.py`。

## 文件清单

| 文件 | 内容 | 规模 |
|---|---|---|
| `test_smoke.jsonl` | 自建中英双语冒烟集（含边界样本：极短文本、长文本、口语/书面、论坛/议论） | 15 条，human 8 / machine 7，短文本 80% |
| `test_hc3_en.jsonl` | HC3 英文真实测试集（人类回答 vs ChatGPT 回答，3 个领域配对） | 198 条，human 99 / machine 99，短文本 54.5% |
| `test_hc3_zh.jsonl` | HC3 中文真实测试集（人类回答 vs ChatGPT 回答，4 个领域配对） | 200 条，human 100 / machine 100，短文本 54.5% |
| `raw_hc3/` | HC3 / HC3-Chinese 原始配对 jsonl（生成测试集的原料） | 7 个分片 |

## 每行格式

```json
{"id": "hc3zh-0001", "text": "…", "label": 1,
 "generator": "chatgpt", "domain": "zh_open_qa",
 "lang": "zh", "source_id": "问题原文", "group": "zh_open_qa::问题原文"}
```

- `label`：0 = human（人类撰写），1 = machine（机器生成）
- `generator`：`human` 或 `chatgpt`
- `domain`：HC3 原始领域（`en_open_qa` / `en_wiki_csai` / `en_medicine` /
  `zh_open_qa` / `zh_baike` / `zh_nlpcc_dbqa` / `zh_law`）
- `group` = `domain::source_id`，同一问题的人类/机器两条共享 group，与训练切分口径一致

## 用法

### 方式一：推理全链路（需要已训练好的模型权重）

```powershell
python scripts/predict.py --input data/test_hc3_zh.jsonl --out-csv result_test.csv `
  --ensemble-dirs data/processed/cls_full_5fold/fold0,data/processed/cls_full_5fold/fold1, `
  data/processed/cls_full_5fold/fold2,data/processed/cls_full_5fold/fold3, `
  data/processed/cls_full_5fold/fold4 `
  --calibration data/processed/cls_full_5fold/calibration.json `
  --stat-model data/processed/stat_feats.joblib --stat-weight 0.3 `
  --max-len 512 --chunk-long
```

因为输入自带 `label`，`predict.py` 推理结束会**自动打印本地宏 F1、短文本 F1、综合分**。
没有训练权重时该命令会报「模型目录不存在」，属正常现象，需先完成训练。

### 方式二：仅评测预测文件（eval.py）

先产出预测 jsonl（每行 `{"id","prob","label","text"}`），再：

```powershell
python scripts/eval.py --pred data/processed/xxx_pred.jsonl
```

`eval.py` 会按赛题口径（宏 F1 × 70% + 短文本 F1 × 30%）自动搜索最优阈值并评分。

## 数据来源与许可

- 英文：Hello-SimpleAI/HC3（open_qa / wiki_csai / medicine 分片）
- 中文：Hello-SimpleAI/HC3-Chinese（open_qa / baike / nlpcc_dbqa / law 分片）
- 许可：CC-BY-SA-4.0；若所依赖的原始子数据集（SQuAD、ELI5 等）许可更严格，以更严格者为准
  （见 HC3 仓库 README「Dataset Copyright」一节）。
- 论文：*How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection*（arXiv:2301.07597）

## 注意

- `test_smoke.jsonl` 中的 machine 样本为**人工模仿的典型机器风格文本**，仅用于快速跑通流程；
  真实机器文本请以 `test_hc3_*.jsonl` 为准。
- 原始数据里含少量 ChatGPT 接口报错文本（"Too many requests" 等），已按常见报错特征过滤，不再出现在测试集中。
- 测试集为随机抽样，不代表官方验证集分布；跨域/跨生成器泛化仍需按 README 的 OOD 流程另行评估。

## 重新生成

```powershell
python scripts/make_test_data.py            # 默认 100 对/语言
python scripts/make_test_data.py --pairs-en 200 --pairs-zh 200 --seed 42
```
