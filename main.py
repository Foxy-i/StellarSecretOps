import pygame
import os
import math
import sys

FPS = 60
WIDTH, HEIGHT = 700, 900
MAX_BG_OFFSET = 40

# 敌人血量
ROCK_HP = 300
ENEMY1_HP = 200
ENEMY2_HP = 150
ENEMY3_HP = 250
ENEMY4_HP = 800
ENEMY6_HP = 280
ENEMY7_HP = 400
ENEMY8_HP = 150
ENEMY13_HP = 200
ENEMY5_HP = 230
ENEMY9_HP = 210
ENEMY10_HP = 230
ENEMY11_HP = 250
ENEMY12_HP = 300
BOSS1_HP = 10000
BOSS2_HP = 12000
BOSS3_HP = 12000
BOSS4_HP = 15000
SP1_HP = 100
SP2_HP = 200
LASERBEAM_DAMAGE = 30
RED_SPEED = -20


# 玩家属性
PLAYER_MAX_HP = 100
PLAYER_LIVES = 3
INVINCIBLE_DURATION = 2000
PLAYER_ULT_CHARGES = 4

# 颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# 关卡阶段
STAGE_1 = 1
STAGE_2 = 2
STAGE_3 = 3
STAGE_4 = 4
STAGE_BOSS = 5
STAGE_WIN = 6

STAGE_DURATION = {
    STAGE_1: 20000,
    STAGE_2: 20000,
    STAGE_3: 20000,
    STAGE_4: 25000,
    STAGE_BOSS: 0,
    STAGE_WIN: 10000,
}

# 游戏状态
STATE_MENU = 0
STATE_LEVEL_SELECT = 1
STATE_PLAYING = 2
STATE_FINAL_WIN = 3   # 最终通关状态

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Stellar Secret Operations (星秘行动)')
clock = pygame.time.Clock()
font = pygame.font.Font('HYPixel11pxU-2.ttf', 20)
title_font = pygame.font.Font('HYPixel11pxU-2.ttf', 50)
menu_font = pygame.font.Font('HYPixel11pxU-2.ttf', 30)

# ------------------------- 图片加载 -------------------------
player1_img = pygame.image.load(os.path.join('gameImages', 'player1.png')).convert()
rock1_img = pygame.image.load(os.path.join('gameImages', 'rock1.png')).convert()
player1_sm_img = pygame.image.load(os.path.join('gameImages', 'player1_sm.png')).convert()
pygame.display.set_icon(player1_sm_img)
# 子弹图片加载区
bullet1_1_img = pygame.image.load(os.path.join('gameImages', 'bullet1.1.png')).convert()
bullet_small_img = pygame.image.load(os.path.join('gameImages', 'bullet1sm.png')).convert()
bullet_small_img = pygame.transform.scale(bullet_small_img, (8, 28))
bullet_small_img.set_colorkey(BLACK)
bullet_small_left_img = pygame.image.load(os.path.join('gameImages', 'bullet1sm_left.png')).convert()
bullet_small_left_img = pygame.transform.scale(bullet_small_left_img, (10, 30))
bullet_small_left_img.set_colorkey(BLACK)
bullet_small_right_img = pygame.image.load(os.path.join('gameImages', 'bullet1sm_right.png')).convert()
bullet_small_right_img = pygame.transform.scale(bullet_small_right_img, (10, 30))
bullet_small_right_img.set_colorkey(BLACK)
bullet2_1_img = pygame.image.load(os.path.join('gameImages', 'bullet2.1.png')).convert_alpha()
bullet2_1_img = pygame.transform.scale(bullet2_1_img, (8, 28))
bullet2_2_img = pygame.image.load(os.path.join('gameImages', 'bullet2.2.png')).convert_alpha()
bullet2_2_img = pygame.transform.scale(bullet2_2_img, (10, 40))
bullet3_1_img = pygame.image.load(os.path.join('gameImages', 'bullet3.1.png')).convert_alpha()
bullet3_1_img = pygame.transform.scale(bullet3_1_img, (8, 40))
bullet3_2_img = pygame.image.load(os.path.join('gameImages', 'bullet3.2.png')).convert_alpha()
bullet3_2_img = pygame.transform.scale(bullet3_2_img, (9, 30))
bullet3_3_img = pygame.image.load(os.path.join('gameImages', 'bullet3.3.png')).convert_alpha()
bullet3_3_img = pygame.transform.scale(bullet3_3_img, (20, 30))
bullet3_4_img = pygame.image.load(os.path.join('gameImages', 'bullet3.4.png')).convert_alpha()
bullet3_4_img = pygame.transform.scale(bullet3_4_img, (27, 30))
missile_track_img = pygame.image.load(os.path.join('gameImages', 'missile_track.png')).convert_alpha()
missile_track_img = pygame.transform.scale(missile_track_img, (7, 14))
wormhole_img = pygame.image.load(os.path.join('gameImages', 'wormhole.png')).convert_alpha()
wormhole_img = pygame.transform.scale(wormhole_img, (80, 80))
enemy_bullet_img = pygame.image.load(os.path.join('gameImages', 'EnemyBullet1.png')).convert()
enemy_bullet2_img = pygame.image.load(os.path.join('gameImages', 'EnemyBullet2.png')).convert_alpha()
enemy_bullet2_img = pygame.transform.scale(enemy_bullet2_img, (10, 25))
enemy_bullet_img3 = pygame.image.load(os.path.join('gameImages', 'EnemyBullet3.png')).convert()
enemy_bullet_laser_img = pygame.image.load(os.path.join('gameImages', 'EnemyBulletLaser.png')).convert_alpha()

laser_frames = []
for i in range(1, 4):
    img = pygame.image.load(os.path.join('gameImages', f'bullet2.3_{i}.png')).convert_alpha()
    img = pygame.transform.scale(img, (12, 40))
    laser_frames.append(img)

enemy1_img = pygame.image.load(os.path.join('gameImages', 'enemy1.png')).convert()
enemy2_img = pygame.image.load(os.path.join('gameImages', 'enemy2.png')).convert()
enemy3_img = pygame.image.load(os.path.join('gameImages', 'enemy3.png')).convert()
enemy4_img = pygame.image.load(os.path.join('gameImages', 'enemy4.png')).convert()
enemy5_img = pygame.image.load(os.path.join('gameImages', 'enemy5.png')).convert()
enemy6_img = pygame.image.load(os.path.join('gameImages', 'enemy6.png')).convert()
enemy7_img = pygame.image.load(os.path.join('gameImages', 'enemy7.png')).convert()
enemy8_img = pygame.image.load(os.path.join('gameImages', 'enemy8.png')).convert()
enemy9_img = pygame.image.load(os.path.join('gameImages', 'enemy9.png')).convert()
enemy10_img = pygame.image.load(os.path.join('gameImages', 'enemy10.png')).convert()
enemy11_img = pygame.image.load(os.path.join('gameImages', 'enemy11.png')).convert()
enemy12_img = pygame.image.load(os.path.join('gameImages', 'enemy12.png')).convert()
enemy13_img = pygame.image.load(os.path.join('gameImages', 'enemy13.png')).convert()
boss_img = pygame.image.load(os.path.join('gameImages', 'boss1.png')).convert()
boss2_img = pygame.image.load(os.path.join('gameImages', 'boss2.png')).convert()
boss3_img = pygame.image.load(os.path.join('gameImages', 'boss3.png')).convert()
boss4_img = pygame.image.load(os.path.join('gameImages', 'boss4.png')).convert()
enemysp1_img = pygame.image.load(os.path.join('gameImages', 'enemysp1.png')).convert()
enemysp2_img = pygame.image.load(os.path.join('gameImages', 'enemysp2.png')).convert()

powerup_img = pygame.image.load(os.path.join('gameImages', 'powerup_yellow.png')).convert()
powerup_img.set_colorkey(BLACK)
powerup_blue_img = pygame.image.load(os.path.join('gameImages', 'powerup_blue.png')).convert_alpha()
powerup_red_img = pygame.image.load(os.path.join('gameImages', 'powerup_red.png')).convert_alpha()

ultimate_ball_img = pygame.image.load(os.path.join('gameImages', 'ultimate_ball.png')).convert_alpha()
ULT_BALL_SIZE = 50
ultimate_ball_img = pygame.transform.scale(ultimate_ball_img, (ULT_BALL_SIZE, ULT_BALL_SIZE))
ultimate_icon_img = pygame.image.load(os.path.join('gameImages', 'ultimate_icon.png')).convert_alpha()
ULT_ICON_SIZE = 20
ultimate_icon_img = pygame.transform.scale(ultimate_icon_img, (ULT_ICON_SIZE, ULT_ICON_SIZE))

overload_img = pygame.image.load(os.path.join('gameImages', 'overload1.png')).convert()
overload_img = pygame.transform.scale(overload_img, (20, 20))
overload_img.set_colorkey(BLACK)
overload2_img = pygame.image.load(os.path.join('gameImages', 'overload2.png')).convert_alpha()
overload2_img = pygame.transform.scale(overload2_img, (8, 16))

life_icon_img = pygame.image.load(os.path.join('gameImages', 'life_icon.png')).convert_alpha()
LIFE_ICON_SIZE = 15
life_icon_img = pygame.transform.scale(life_icon_img, (LIFE_ICON_SIZE, LIFE_ICON_SIZE))

hp_icon_img = pygame.image.load(os.path.join('gameImages', 'hp_icon.png')).convert_alpha()
HP_ICON_WIDTH = 12
HP_ICON_HEIGHT = 24
hp_icon_img = pygame.transform.scale(hp_icon_img, (HP_ICON_WIDTH, HP_ICON_HEIGHT))

mission_start_img = pygame.image.load(os.path.join('gameImages', 'Commander_mission_start.png')).convert_alpha()
mission_start_img = pygame.transform.scale(mission_start_img, (250, 45))   # 可根据需要调整尺寸
player_yes_img = pygame.image.load(os.path.join('gameImages', 'Player_yes.png')).convert_alpha()
player_yes_img = pygame.transform.scale(player_yes_img, (150, 45))         # 可调整
mission_start_pos = (0, 50)   # 左上角坐标，可自行调整
player_yes_pos = (0, 50)

explosion_frames = []
for i in range(1, 13):
    filename = f'explosion_{i:02d}.png'
    path = os.path.join('gameImages', filename)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (400, 400))
    explosion_frames.append(img)

hit_explode_frames = []
for i in range(1, 11):
    filename = f'hit_explode{i}.png'
    path = os.path.join('gameImages', filename)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (20, 20))
    hit_explode_frames.append(img)

enemy_explode_frames = []
for i in range(1, 11):
    filename = f'enemy_explode{i}.png'
    path = os.path.join('gameImages', filename)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (100, 100))
    enemy_explode_frames.append(img)

NukeBullet_img = pygame.image.load(os.path.join('gameImages', 'NukeBullet.png')).convert()

# 背景图片
menu_bg = pygame.image.load(os.path.join('gameImages', 'background0.png')).convert()
menu_bg = pygame.transform.scale(menu_bg, (WIDTH, HEIGHT))
menu_bg_double = pygame.Surface((WIDTH * 2, HEIGHT))
menu_bg_double.blit(menu_bg, (0, 0))
menu_bg_double.blit(menu_bg, (WIDTH, 0))

bg_full = pygame.image.load(os.path.join('gameImages', 'background1.png')).convert()
bg_scale_h = HEIGHT
bg_scale_w = int(bg_full.get_width() * HEIGHT / bg_full.get_height())
bg_scaled = pygame.transform.scale(bg_full, (bg_scale_w, bg_scale_h))
target_w = WIDTH + 2 * MAX_BG_OFFSET
if bg_scale_w > target_w:
    left = (bg_scale_w - target_w) // 2
    background_img1 = bg_scaled.subsurface(pygame.Rect(left, 0, target_w, HEIGHT)).copy()
else:
    background_img1 = pygame.Surface((target_w, HEIGHT))
    background_img1.fill(BLACK)
    background_img1.blit(bg_scaled, ((target_w - bg_scale_w) // 2, 0))

bg2_full = pygame.image.load(os.path.join('gameImages', 'background2.png')).convert()
bg2_scale_w = int(bg2_full.get_width() * HEIGHT / bg2_full.get_height())
bg2_scaled = pygame.transform.scale(bg2_full, (bg2_scale_w, HEIGHT))
if bg2_scale_w > target_w:
    left = (bg2_scale_w - target_w) // 2
    background_img2 = bg2_scaled.subsurface(pygame.Rect(left, 0, target_w, HEIGHT)).copy()
else:
    background_img2 = pygame.Surface((target_w, HEIGHT))
    background_img2.fill(BLACK)
    background_img2.blit(bg2_scaled, ((target_w - bg2_scale_w) // 2, 0))

bg3_full = pygame.image.load(os.path.join('gameImages', 'background3.png')).convert()
bg3_scale_w = int(bg3_full.get_width() * HEIGHT / bg3_full.get_height())
bg3_scaled = pygame.transform.scale(bg3_full, (bg3_scale_w, HEIGHT))
if bg3_scale_w > target_w:
    left = (bg3_scale_w - target_w) // 2
    background_img3 = bg3_scaled.subsurface(pygame.Rect(left, 0, target_w, HEIGHT)).copy()
else:
    background_img3 = pygame.Surface((target_w, HEIGHT))
    background_img3.fill(BLACK)
    background_img3.blit(bg3_scaled, ((target_w - bg3_scale_w) // 2, 0))

bg4_full = pygame.image.load(os.path.join('gameImages', 'background4.png')).convert()
bg4_scale_w = int(bg4_full.get_width() * HEIGHT / bg4_full.get_height())
bg4_scaled = pygame.transform.scale(bg4_full, (bg4_scale_w, HEIGHT))
if bg4_scale_w > target_w:
    left = (bg4_scale_w - target_w) // 2
    background_img4 = bg4_scaled.subsurface(pygame.Rect(left, 0, target_w, HEIGHT)).copy()
else:
    background_img4 = pygame.Surface((target_w, HEIGHT))
    background_img4.fill(BLACK)
    background_img4.blit(bg4_scaled, ((target_w - bg4_scale_w) // 2, 0))

background_img = background_img1
bg1_y = 0
bg2_y = -HEIGHT
bg_speed = 0.5
menu_bg_x = 0
menu_bg_speed = -1

# 精灵组
all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
enemy1_group = pygame.sprite.Group()
enemy2_group = pygame.sprite.Group()
enemy3_group = pygame.sprite.Group()
enemy4_group = pygame.sprite.Group()
enemy6_group = pygame.sprite.Group()
enemy7_group = pygame.sprite.Group()
enemy8_group = pygame.sprite.Group()
enemy13_group = pygame.sprite.Group()
enemy5_group = pygame.sprite.Group()
enemy9_group = pygame.sprite.Group()
enemy10_group = pygame.sprite.Group()
enemy11_group = pygame.sprite.Group()
enemy12_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
special_enemies = pygame.sprite.Group()

game_state = STATE_MENU
current_level = 1
unlocked_levels = 1

game_stage = STAGE_1
stage_start_time = 0
game_over = False
shoot_cooldown = 120
last_shoot = 0
space_was_pressed = False
boss_spawned = False
triggered_events = {}
player = None
bg_offset = 0
last_bg_offset = 0
game_over_start = 0

player_explosion_frames = []
for i in range(1, 11):
    filename = f'player_explode{i}.png'
    path = os.path.join('gameImages', filename)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (120, 120))
    player_explosion_frames.append(img)

# 缩小版玩家爆炸（用于火箭弹命中玩家）
small_player_explosion_frames = []
for i in range(1, 11):
    filename = f'player_explode{i}.png'
    path = os.path.join('gameImages', filename)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (60, 60))  # 缩小版
    small_player_explosion_frames.append(img)

player_laser_frames = []
for i in range(1, 7):
    img = pygame.image.load(os.path.join('gameImages', f'player_laser{i}.png')).convert_alpha()
    img = pygame.transform.scale(img, (70, 100))
    player_laser_frames.append(img)

level_stage_events = {
    1: {
        STAGE_1: [
            # (0, lambda: spawn_enemy4([110])),
            (2000, lambda: spawn_enemy1([110, 510])),
            (4000, lambda: spawn_sp1(100, "yellow")),
            (3000, lambda: spawn_enemy1([210, 410])),
            (4000, lambda: spawn_enemy1([110, 510])),
            (6000, lambda: spawn_sp1(650, "blue")),
            (8000, lambda: spawn_enemy2([200, 500])),
            (9000, lambda: spawn_enemy2([50, 650])),
            (11000, lambda: spawn_sp2(200)),
            (13000, lambda: spawn_enemy1([100, 250, 400, 550])),
            (15000, lambda: spawn_sp1(600, "red")),
            (17200, lambda: spawn_enemy1([150])),
            (17400, lambda: spawn_enemy1([100])),
            (17600, lambda: spawn_enemy1([50])),
            (17800, lambda: spawn_enemy1([0])),
            (18000, lambda: spawn_enemy1([-50])),
            (17200, lambda: spawn_enemy1([450])),
            (17400, lambda: spawn_enemy1([500])),
            (17600, lambda: spawn_enemy1([550])),
            (17800, lambda: spawn_enemy1([600])),
            (18000, lambda: spawn_enemy1([650])),
            (19000, lambda: spawn_sp1(200, "yellow")),
        ],
        STAGE_2: [
            (3000, lambda: spawn_sp1(350, "yellow")),
            (3000, lambda: spawn_enemy7([550])),
            (3000, lambda: spawn_enemy1([150])),
            (3400, lambda: spawn_enemy1([150])),
            (9000, lambda: spawn_enemy7([100])),
            (9000, lambda: spawn_enemy1([550])),
            (9400, lambda: spawn_enemy1([550])),
            (12000, lambda: spawn_enemy7([550])),
            (12000, lambda: spawn_enemy1([150])),
            (12400, lambda: spawn_enemy1([150])),
            (15000, lambda: spawn_enemy2([200, 350, 500])),
            (14000, lambda: spawn_sp1(0, "red")),
            (18000, lambda: spawn_enemy1([200])),
            (18200, lambda: spawn_enemy1([200])),
            (18400, lambda: spawn_enemy1([200])),
            (18600, lambda: spawn_enemy1([200])),
            (18800, lambda: spawn_enemy1([200])),
            (19000, lambda: spawn_enemy1([200])),
            (19000, lambda: spawn_sp1(670, "blue")),
            (19000, lambda: spawn_enemy1([500])),
            (19200, lambda: spawn_enemy1([500])),
            (19400, lambda: spawn_enemy1([500])),
            (19600, lambda: spawn_enemy1([500])),
            (19800, lambda: spawn_enemy1([500])),
            (20000, lambda: spawn_enemy1([500])),
            (20000, lambda: spawn_sp1(350, "yellow")),
            (20000, lambda: spawn_sp2(600)),
        ],
        STAGE_3: [
            (1000, lambda: spawn_sp1(50, "yellow")),
            (1000, lambda: spawn_enemy1([100, 200, 300, 400, 500])),
            (3000, lambda: spawn_enemy2([150, 250, 350, 450])),
            (7000, lambda: spawn_enemy1([200, 300, 400])),
            (9000, lambda: spawn_enemy6([300])),
            (10000, lambda: spawn_sp1(100, "blue")),
            (11000, lambda: spawn_sp2(350)),
            (13000, lambda: spawn_enemy6([200, 400])),
            (15000, lambda: spawn_enemy2([200, 350, 500])),
            (19000, lambda: spawn_enemy1([100, 250, 400, 550])),
        ],
        STAGE_4: [
            (1000, lambda: spawn_sp1(0, "yellow")),
            (2000, lambda: spawn_enemy6([200])),
            (3000, lambda: spawn_enemy6([500])),
            (4000, lambda: spawn_enemy6([200])),
            (5000, lambda: spawn_enemy6([500])),
            (7000, lambda: spawn_enemy2([300])),
            (7200, lambda: spawn_enemy2([250, 350])),
            (8000, lambda: spawn_enemy7([200,400])),
            (9000, lambda: spawn_enemy4([350])),
            (11000, lambda: spawn_sp2(380)),
            (13000, lambda: spawn_enemy1([200, 300, 400])),
            (14000, lambda: spawn_sp1(600, "red")),
            (16000, lambda: spawn_enemy4([175, 525])),
        ],
        STAGE_BOSS: [],
        STAGE_WIN: [],
    },
    2: {
        STAGE_1: [
            (1000, lambda: spawn_sp1(0, "yellow")),
            (2000, lambda: spawn_enemy13([600])),
            (4000, lambda: spawn_enemy13([100, 550, 650])),
            (6000, lambda: spawn_enemy13([50, 150])),
            (8000, lambda: spawn_enemy13([600])),
            (10000, lambda: spawn_enemy13([100])),
            (12000, lambda: spawn_enemy13([600])),
            (14000, lambda: spawn_enemy13([150])),
            (14200, lambda: spawn_enemy13([150])),
            (14400, lambda: spawn_enemy13([150])),
            (14600, lambda: spawn_enemy13([150])),
            (15600, lambda: spawn_enemy13([500])),
            (15800, lambda: spawn_enemy13([500])),
            (16000, lambda: spawn_enemy13([500])),
            (16200, lambda: spawn_enemy13([500])),
            (16500, lambda: spawn_sp1(0, "red")),
            (18000, lambda: spawn_enemy6([200])),
            (18100, lambda: spawn_enemy6([450])),
            (19000, lambda: spawn_enemy6([100])),
            (19100, lambda: spawn_enemy6([500])),
        ],
        STAGE_2: [
            (1000, lambda: spawn_sp1(0, "red")),
            (3000, lambda: spawn_enemy3([150])),
            (4000, lambda: spawn_rocks([100, 200, 300])),
            (5000, lambda: spawn_enemy3([200, 500])),
            (9000, lambda: spawn_enemy8([250, 450])),
            (10000, lambda: spawn_sp1(400, "blue")),
            (11000, lambda: spawn_sp2(300)),
            (13000, lambda: spawn_enemy8([100, 300, 500])),
            (15000, lambda: spawn_enemy1([150, 250, 350, 450, 550])),
            (19000, lambda: spawn_enemy3([200, 400])),
        ],
        STAGE_3: [
            (1000, lambda: spawn_sp1(620, "red")),
            (1000, lambda: spawn_enemy13([100, 200, 300, 400, 500])),
            (3000, lambda: spawn_enemy8([150, 450])),
            (7000, lambda: spawn_enemy5([200])),
            (9000, lambda: spawn_enemy5([400])),
            (11000, lambda: spawn_sp2(600)),
            (13000, lambda: spawn_enemy9([150, 550])),
            (15000, lambda: spawn_enemy8([50, 350, 650])),
            (16000, lambda: spawn_sp1(300, "yellow")),

            (15000, lambda: spawn_enemy8([0, 100, 200, 300, 400, 500, 600, 700])),
            (16000, lambda: spawn_rocks([100, 600])),
            (19000, lambda: spawn_enemy3([100, 4800])),
            (19800, lambda: spawn_enemy3([150, 530])),
        ],
        STAGE_4: [
            (600, lambda: spawn_enemy3([100, 480])),
            (1400, lambda: spawn_enemy3([150, 530])),
            (2200, lambda: spawn_enemy3([100, 480])),
            (3000, lambda: spawn_enemy3([150, 530])),

            (2000, lambda: spawn_sp1(270, "yellow")),
            (5500, lambda: spawn_enemy11([200])),

            (7000, lambda: spawn_enemy11([500])),
            (9000, lambda: spawn_enemy5([175])),
            (9500, lambda: spawn_enemy5([525])),
            (11000, lambda: spawn_sp2(400)),
            (13000, lambda: spawn_enemy3([200, 300, 400])),
            (15000, lambda: spawn_enemy12([50, 500])),

            (16000, lambda: spawn_rocks([200, 300])),
            (17000, lambda: spawn_rocks([600, 500])),

            (19000, lambda: spawn_rocks([100, 200, 300, 400, 500, 600])),
            (19000, lambda: spawn_sp1(490, "blue")),
        ],
        STAGE_BOSS: [],
        STAGE_WIN: [],
    },
    3: {
        STAGE_1: [
            (1000, lambda: spawn_sp1(350, "red")),
            (1000, lambda: spawn_sp1(300, "red")),
            (1000, lambda: spawn_sp1(250, "red")),

            (2000, lambda: spawn_enemy10([600])),
            (2500, lambda: spawn_enemy10([50])),
            (3000, lambda: spawn_enemy10([500])),
            (3500, lambda: spawn_enemy10([150])),
            (4000, lambda: spawn_enemy10([400])),
            (4500, lambda: spawn_enemy10([250])),
            (5000, lambda: spawn_enemy10([300])),
            (5000, lambda: spawn_enemy10([350])),

            (7000, lambda: spawn_enemy11([400])),
            (7000, lambda: spawn_enemy11([250])),
            (7000, lambda: spawn_sp1(50, "blue")),

            (10000, lambda: spawn_enemy12([500])),
            (10000, lambda: spawn_enemy12([-30])),

            (13000, lambda: spawn_enemy5([0, 200, 400, 600])),
            (15000, lambda: spawn_enemy13([0, 200, 400, 600])),
            (16000, lambda: spawn_enemy13([0, 200, 400, 600])),

            (18000, lambda: spawn_sp1(700, "yellow")),
            (18000, lambda: spawn_sp1(600, "yellow")),
            (18000, lambda: spawn_sp2(50)),
            (18000, lambda: spawn_sp2(150)),

        ],
        STAGE_2: [
            (2000, lambda: spawn_enemy9([600])),
            (2500, lambda: spawn_enemy10([50])),
            (3000, lambda: spawn_enemy10([500])),
            (3500, lambda: spawn_enemy9([150])),
            (4000, lambda: spawn_enemy9([400])),
            (4500, lambda: spawn_enemy10([250])),
            (5000, lambda: spawn_enemy10([300])),
            (5000, lambda: spawn_enemy9([350])),

            (6000, lambda: spawn_sp1(700, "blue")),
            (6000, lambda: spawn_sp1(0, "red")),

            (7000, lambda: spawn_enemy9([350])),
            (7500, lambda: spawn_enemy10([300])),
            (8000, lambda: spawn_enemy10([250])),
            (8500, lambda: spawn_enemy9([400])),
            (9000, lambda: spawn_enemy9([150])),
            (9500, lambda: spawn_enemy10([500])),
            (10000, lambda: spawn_enemy10([50])),
            (10000, lambda: spawn_enemy9([600])),

            (12000, lambda: spawn_enemy8([600])),
            (12500, lambda: spawn_enemy8([50])),
            (13000, lambda: spawn_enemy8([500])),
            (13500, lambda: spawn_enemy8([150])),

            (14000, lambda: spawn_enemy6([400])),
            (14500, lambda: spawn_enemy6([250])),
            (15000, lambda: spawn_enemy6([300])),
            (15000, lambda: spawn_enemy6([350])),

            (17000, lambda: spawn_enemy7([400])),
            (17000, lambda: spawn_enemy7([250])),

            (17500, lambda: spawn_enemy7([600])),
            (17500, lambda: spawn_enemy7([50])),

            (18000, lambda: spawn_sp2(0)),
            (19000, lambda: spawn_sp2(550)),


        ],
        STAGE_3: [
            (2000, lambda: spawn_enemy13([600])),
            (2500, lambda: spawn_enemy13([50])),
            (3000, lambda: spawn_enemy13([600])),
            (3500, lambda: spawn_enemy13([50])),
            (4000, lambda: spawn_enemy13([600])),
            (4500, lambda: spawn_enemy13([50])),

            (2000, lambda: spawn_enemy8([500])),

            (3000, lambda: spawn_enemy8([150])),

            (4000, lambda: spawn_enemy8([500])),

            (6000, lambda: spawn_enemy8([150])),

            (5000, lambda: spawn_sp1(50, "blue")),
            (6000, lambda: spawn_sp1(600, "yellow")),

            (7000, lambda: spawn_enemy11([450])),

            (8000, lambda: spawn_enemy11([200])),

            (9000, lambda: spawn_enemy11([250])),

            (10000, lambda: spawn_enemy11([650])),


            (12000, lambda: spawn_enemy13([600])),
            (12500, lambda: spawn_enemy13([50])),
            (13000, lambda: spawn_enemy13([500])),
            (13500, lambda: spawn_enemy13([150])),

            (14000, lambda: spawn_enemy4([400])),
            (15000, lambda: spawn_sp1(50, "red")),
            (15000, lambda: spawn_sp1(600, "yellow")),

            (16000, lambda: spawn_enemy4([300])),

            (17000, lambda: spawn_enemy3([400])),
            (17000, lambda: spawn_enemy8([320])),
            (17000, lambda: spawn_enemy3([250])),

            (18000, lambda: spawn_enemy12([50])),
            (19000, lambda: spawn_enemy12([600])),

            (18000, lambda: spawn_sp2(0)),
            (19000, lambda: spawn_sp2(550)),
        ],
        STAGE_4: [
            (1000, lambda: spawn_sp1(350, "blue")),
            (1000, lambda: spawn_sp1(300, "blue")),
            (1000, lambda: spawn_sp1(250, "blue")),

            (2000, lambda: spawn_enemy5([600])),
            (2500, lambda: spawn_enemy5([50])),
            (3000, lambda: spawn_enemy5([600])),
            (3500, lambda: spawn_enemy5([50])),
            (4000, lambda: spawn_enemy5([600])),
            (4500, lambda: spawn_enemy5([50])),

            (2000, lambda: spawn_enemy8([500])),

            (3000, lambda: spawn_enemy8([150])),

            (4000, lambda: spawn_enemy8([500])),

            (6000, lambda: spawn_enemy8([150])),

            (5000, lambda: spawn_sp1(50, "blue")),
            (6000, lambda: spawn_sp1(600, "yellow")),

            (7000, lambda: spawn_enemy10([450])),

            (8000, lambda: spawn_enemy10([200])),

            (9000, lambda: spawn_enemy10([250])),

            (10000, lambda: spawn_enemy10([650])),


            (12000, lambda: spawn_enemy7([600])),
            (12500, lambda: spawn_enemy7([50])),
            (13000, lambda: spawn_enemy7([500])),
            (13500, lambda: spawn_enemy7([150])),

            (14000, lambda: spawn_enemy3([400])),
            (15000, lambda: spawn_sp1(50, "red")),
            (15000, lambda: spawn_sp1(600, "yellow")),

            (16000, lambda: spawn_enemy4([300])),

            (17000, lambda: spawn_enemy9([400])),
            (17000, lambda: spawn_enemy8([320])),
            (17000, lambda: spawn_enemy9([250])),

            (18000, lambda: spawn_enemy1([50])),
            (19000, lambda: spawn_enemy1([600])),

            (18000, lambda: spawn_sp2(0)),
            (19000, lambda: spawn_sp2(550)),
        ],
        STAGE_BOSS: [],
        STAGE_WIN: [],
    },
    4: {
        STAGE_1: [],
        STAGE_2: [],
        STAGE_3: [],
        STAGE_4: [],
        STAGE_BOSS: [],
        STAGE_WIN: [],
    },
}

# 游戏类
class EnemyBase(pygame.sprite.Sprite):
    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.max_hp = hp
        self.is_boss = False

    def kill(self):
        if not self.alive():
            return
        if not self.is_boss:
            effect = EnemyExplosion(self.rect.centerx, self.rect.centery)
            all_sprites.add(effect)
        super().kill()

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()


class Rock(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ROCK_HP)
        self.image_ori = pygame.transform.scale(rock1_img, (70, 80))
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.9 / 2
        self.rect.x = spawn_x
        self.rect.y = -80
        self.speedy = 3
        self.total_degree = 0
        self.rot_degree = 2

    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree %= 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy1(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY1_HP)
        self.image = pygame.transform.scale(enemy1_img, (60, 60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.x = spawn_x
        self.rect.y = -60
        self.speedy = 4
        self.shoot_cd = 3000
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_cd:
            eb = EnemyBullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(eb)
            enemy_bullets.add(eb)
            self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy2(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY2_HP)
        self.image = pygame.transform.scale(enemy2_img, (70, 85))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.x = spawn_x
        self.rect.y = -70
        self.fast_speed = 9
        self.normal_speed = 2
        self.mid_y = HEIGHT // 3
        self.pass_mid = False
        self.shoot_cd = 1800
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd
        self.has_shot = False

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_cd:
            eb_left = EnemyBullet(self.rect.centerx - 8, self.rect.bottom)
            all_sprites.add(eb_left)
            enemy_bullets.add(eb_left)
            eb_right = EnemyBullet(self.rect.centerx + 8, self.rect.bottom)
            all_sprites.add(eb_right)
            enemy_bullets.add(eb_right)
            self.last_shoot = now

    def update(self):
        if not self.pass_mid:
            self.rect.y += self.fast_speed
            if self.rect.y >= self.mid_y:
                self.pass_mid = True
        else:
            self.rect.y += self.normal_speed
            if not self.has_shot:
                self.enemy_shoot()
                self.has_shot = True
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy3(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY3_HP)
        self.image = pygame.transform.scale(enemy3_img, (110, 83))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 28
        self.rect.x = spawn_x
        self.rect.y = -70
        self.speedy = 2
        self.shoot_cd = 2200
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd

        self.burst_count = 0
        self.burst_delay = 150      # 每排间隔，可调
        self.burst_timer = 0

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        if self.burst_count == 0 and now - self.last_shoot > self.shoot_cd:
            self.burst_count = 1
            self.burst_timer = now

        if self.burst_count > 0:
            if now - self.burst_timer >= self.burst_delay:
                left_bullet = EnemyBullet(self.rect.centerx - 10, self.rect.bottom)
                right_bullet = EnemyBullet(self.rect.centerx + 10, self.rect.bottom)
                all_sprites.add(left_bullet, right_bullet)
                enemy_bullets.add(left_bullet, right_bullet)

                self.burst_count += 1
                self.burst_timer = now
                if self.burst_count > 3:          # 3排射完
                    self.burst_count = 0
                    self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy4(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY4_HP)
        self.image = pygame.transform.scale(enemy4_img, (WIDTH // 2, 150))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn_x
        self.rect.y = -120
        self.speedy = 0.8
        self.shoot_cd = 2200
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd
        self.bullet_count = 12
        self.bullet_speed = 5
        hit_w = 250
        hit_h = 60
        self.hitbox_rect = pygame.Rect(0, 0, hit_w, hit_h)
        self.hitbox_rect.center = self.rect.center

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change
        self.hitbox_rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_cd:
            start_angle = 0
            end_angle = math.pi
            for i in range(self.bullet_count):
                angle = start_angle + (end_angle - start_angle) * i / (self.bullet_count - 1)
                speed_x = self.bullet_speed * math.cos(angle)
                speed_y = self.bullet_speed * math.sin(angle)
                eb = EnemyBullet(self.rect.centerx - 10, self.rect.bottom - 30)
                eb.speed_x = speed_x
                eb.speedy = speed_y
                all_sprites.add(eb)
                enemy_bullets.add(eb)
            self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.hitbox_rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()
        self.enemy_shoot()


class Enemy5(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY5_HP)
        self.image = pygame.transform.scale(enemy5_img, (230, 120))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # enemy5使用矩形碰撞，不设置radius
        self.rect.x = spawn_x
        self.rect.y = -80
        self.speedy = 1.5
        self.shoot_cd = 2800
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd
        self.burst_count = 0
        self.burst_delay = 200
        self.burst_timer = 0

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        if self.burst_count == 0 and now - self.last_shoot > self.shoot_cd:
            self.burst_count = 1
            self.burst_timer = now
        if self.burst_count > 0:
            if now - self.burst_timer >= self.burst_delay:
                eb = EnemyBullet2(self.rect.centerx, self.rect.bottom)
                all_sprites.add(eb)
                enemy_bullets.add(eb)
                self.burst_count += 1
                self.burst_timer = now
                if self.burst_count > 3:
                    self.burst_count = 0
                    self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy6(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY6_HP)
        self.image = pygame.transform.scale(enemy6_img, (135, 120))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 27
        self.rect.x = spawn_x
        self.rect.y = -70
        self.speedy = 2
        self.shoot_cd = 2000
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd

        # 所有子弹的相对位置
        self.bullet_offset = [
            (-22, -18), (-11, -8),
            (-10, 5),
            (10, 5),
            (11, -8), (22, -18)
        ]
        self.burst_size = 2           # 每排发射的子弹数（位置数）
        self.burst_delay = 150
        self.burst_index = 0
        self.burst_active = False
        self.burst_timer = 0

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        if not self.burst_active and now - self.last_shoot > self.shoot_cd:
            self.burst_active = True
            self.burst_index = 0
            self.burst_timer = now

        if self.burst_active:
            if now - self.burst_timer >= self.burst_delay:
                # 发射本排的子弹
                for i in range(self.burst_size):
                    idx = self.burst_index + i
                    if idx >= len(self.bullet_offset):
                        break
                    off_x, off_y = self.bullet_offset[idx]
                    bullet_x = self.rect.centerx + off_x
                    bullet_y = self.rect.bottom + off_y
                    eb = EnemyBullet(bullet_x, bullet_y)
                    all_sprites.add(eb)
                    enemy_bullets.add(eb)

                self.burst_index += self.burst_size
                self.burst_timer = now

                if self.burst_index >= len(self.bullet_offset):
                    self.burst_active = False
                    self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy7(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY7_HP)
        self.image = pygame.transform.scale(enemy7_img, (160, 170))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 35
        self.rect.x = spawn_x
        self.rect.y = -80
        self.speedy = 2.5
        self.shoot_cd = 2500
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd

        # 爆发模式相关变量
        self.burst_count = 0           # 当前第几排
        self.burst_delay = 60         # 每排间隔（毫秒），可根据需要调整
        self.burst_timer = 0

        self.side_space = 35          # 左右子弹距离中心的水平偏移

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        # 冷却完毕，启动爆发
        if self.burst_count == 0 and now - self.last_shoot > self.shoot_cd:
            self.burst_count = 1
            self.burst_timer = now

        # 爆发进行中
        if self.burst_count > 0:
            if now - self.burst_timer >= self.burst_delay:
                # 发射左右各一发
                left_eb = EnemyBullet(self.rect.centerx - self.side_space, self.rect.bottom - 10)
                right_eb = EnemyBullet(self.rect.centerx + self.side_space, self.rect.bottom - 10)
                all_sprites.add(left_eb, right_eb)
                enemy_bullets.add(left_eb, right_eb)

                self.burst_count += 1
                self.burst_timer = now

                # 打完5排，爆发结束，重置冷却
                if self.burst_count > 5:
                    self.burst_count = 0
                    self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy8(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY8_HP)
        self.image = pygame.transform.scale(enemy8_img, (70, 70))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 22
        self.rect.x = spawn_x
        self.rect.y = -60
        self.attack_speed = 10

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def update(self):
        self.rect.y += self.attack_speed
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy9(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY9_HP)
        self.image = pygame.transform.scale(enemy9_img, (70, 90))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.x = spawn_x
        self.rect.y = -80
        self.speedy = 4
        self.shoot_cd = 5000
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_cd:
            eb_left = EnemyBullet2(self.rect.centerx - 22, self.rect.bottom)
            all_sprites.add(eb_left)
            enemy_bullets.add(eb_left)
            eb_right = EnemyBullet2(self.rect.centerx + 22, self.rect.bottom)
            all_sprites.add(eb_right)
            enemy_bullets.add(eb_right)
            self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy10(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY10_HP)
        self.image = pygame.transform.scale(enemy10_img, (100, 80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 32
        self.rect.x = spawn_x
        self.rect.y = -80
        self.speedy = 3
        self.shoot_cd = 2200
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd
        # 新增爆发相关变量
        self.burst_count = 0          # 当前爆发第几排
        self.burst_delay = 300        # 每排之间的间隔（毫秒）
        self.burst_timer = 0

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        # 如果冷却完毕，启动爆发
        if self.burst_count == 0 and now - self.last_shoot > self.shoot_cd:
            self.burst_count = 1
            self.burst_timer = now

        # 爆发进行中
        if self.burst_count > 0:
            if now - self.burst_timer >= self.burst_delay:
                # 每排发射左右两颗子弹（和原来位置一样）
                left_bullet = EnemyBullet2(self.rect.centerx - 25, self.rect.bottom)
                right_bullet = EnemyBullet2(self.rect.centerx + 25, self.rect.bottom)
                all_sprites.add(left_bullet, right_bullet)
                enemy_bullets.add(left_bullet, right_bullet)

                self.burst_count += 1
                self.burst_timer = now

                # 打完 3 排，爆发结束，重置冷却
                if self.burst_count > 3:
                    self.burst_count = 0
                    self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy11(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY11_HP)
        self.image = pygame.transform.scale(enemy11_img, (140, 150))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 55
        self.rect.centerx = spawn_x
        self.rect.y = -120
        self.speedy = 2
        self.shoot_cd = 2200
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd
        self.bullet_count = 12
        self.bullet_speed = 5
        self.offset_left = -35
        self.offset_right = 35

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_cd:
            for origin_x in [self.rect.centerx + self.offset_left, self.rect.centerx + self.offset_right]:
                start_angle = 0
                end_angle = math.pi
                for i in range(self.bullet_count):
                    angle = start_angle + (end_angle - start_angle) * i / (self.bullet_count - 1)
                    speed_x = self.bullet_speed * math.cos(angle)
                    speed_y = self.bullet_speed * math.sin(angle)
                    eb = EnemyBullet(origin_x, self.rect.bottom - 30)
                    eb.speed_x = speed_x
                    eb.speedy = speed_y
                    all_sprites.add(eb)
                    enemy_bullets.add(eb)
            self.last_shoot = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy12(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY12_HP)
        self.image = pygame.transform.scale(enemy12_img, (225, 250))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 35
        self.rect.x = spawn_x
        self.rect.y = -100
        self.speedy = 1
        self.laser_cd = 4000
        self.last_laser = pygame.time.get_ticks() - self.laser_cd
        self.active_laser = None

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def enemy_shoot(self):
        if self.rect.bottom >= HEIGHT:
            return
        now = pygame.time.get_ticks()
        if now - self.last_laser > self.laser_cd:
            laser_left = EnemyLaserBeam(self.rect.centerx - 70, self.rect.bottom, self)
            laser_right = EnemyLaserBeam(self.rect.centerx + 35, self.rect.bottom, self)
            all_sprites.add(laser_left, laser_right)
            enemy_bullets.add(laser_left, laser_right)
            self.last_laser = now

    def update(self):
        self.rect.y += self.speedy
        self.enemy_shoot()
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy13(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(ENEMY13_HP)
        self.image_ori = pygame.transform.scale(enemy13_img, (60, 60))
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.x = spawn_x
        self.rect.y = -60
        self.speed = 1.5
        self.shoot_cd = 2000
        self.last_shoot = pygame.time.get_ticks() - self.shoot_cd

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def update(self):
        self.rect.y += self.speed
        if player and not player.dying:
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            angle = math.degrees(math.atan2(dx, dy))
            ANGLE_OFFSET = 0
            self.image = pygame.transform.rotate(self.image_ori, angle + ANGLE_OFFSET)
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        else:
            self.image = self.image_ori.copy()
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_cd:
            self.shoot_targeted()
            self.last_shoot = now
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

    def shoot_targeted(self):
        if not player or player.dying:
            return
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist == 0:
            return
        bullet_speed = 7
        vx = (dx / dist) * bullet_speed
        vy = (dy / dist) * bullet_speed
        eb = EnemyBullet(self.rect.centerx, self.rect.centery)
        eb.speed_x = vx
        eb.speedy = vy
        all_sprites.add(eb)
        enemy_bullets.add(eb)


class EnemySp1(EnemyBase):
    def __init__(self, spawn_x, drop_color='yellow'):
        super().__init__(SP1_HP)
        self.drop_color = drop_color
        self.image = pygame.transform.scale(enemysp1_img, (74, 95))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.x = spawn_x
        self.rect.y = -60
        self.speedy = 1

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

    def kill(self):
        if not self.alive():
            return
        drop = PowerUp(self.rect.centerx, self.rect.centery, self.drop_color, color_cycle=True)
        all_sprites.add(drop)
        powerups.add(drop)
        super().kill()


class EnemySp2(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(SP2_HP)
        self.image = pygame.transform.scale(enemysp2_img, (60, 70))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.x = spawn_x
        self.rect.y = -60
        self.speedy = 1

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

    def kill(self):
        if not self.alive():
            return
        drop = PowerUp(self.rect.centerx, self.rect.centery, 'ultimate')
        all_sprites.add(drop)
        powerups.add(drop)
        super().kill()


class Boss1(EnemyBase):
    def __init__(self):
        super().__init__(BOSS1_HP)
        self.is_boss = True
        boss_scale_h = 220
        boss_scale_w = 420
        self.image = pygame.transform.scale(boss_img, (boss_scale_w, boss_scale_h))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = min(boss_scale_w, boss_scale_h) // 2
        self.entering = True
        self.enter_speed = 2
        self.enter_target_y = 30
        self.rect.x = WIDTH // 2 - boss_scale_w // 2
        self.rect.y = -boss_scale_h
        self.speed_x = 1.5
        self.speed_y = 1
        self.move_area = pygame.Rect(20, self.enter_target_y, WIDTH - 40, 350)
        self.mode = 1
        self.attack_interval = 3000
        self.next_attack = 0
        self.explosion_played = False
        self.frozen = False
        self.frozen_until = 0

        # 分批次攻击相关变量（仅模式1、2使用）
        self.attack_active = False       # 是否正在进行分批次攻击
        self.current_attack_mode = None  # 当前执行的攻击模式
        self.burst_count = 0             # 当前攻击的批次计数
        self.burst_timer = 0             # 批次间隔计时器
        self.burst_delay = 150           # 每批次间隔（毫秒，数值越小发射越快）

    # 模式1：横向双排分2批发射，每次1排
    def burst_shoot_mode1(self, burst_count):
        bullet_width = 16
        start_x = self.rect.left + bullet_width // 2
        end_x = self.rect.right - bullet_width // 2
        if end_x - start_x < bullet_width * 9:
            start_x = self.rect.centerx - bullet_width * 5
            end_x = self.rect.centerx + bullet_width * 5
        step = (end_x - start_x) / 9
        y_offsets = [self.rect.bottom + 5, self.rect.bottom + 21]
        if burst_count < len(y_offsets):
            y_off = y_offsets[burst_count]
            for i in range(10):
                x_pos = start_x + i * step
                eb = EnemyBullet(x_pos, y_off)
                eb.speedy = 7
                eb.speed_x = 0
                all_sprites.add(eb)
                enemy_bullets.add(eb)

    # 模式2：矩阵弹幕分10批发射，每次1排
    def burst_shoot_mode2(self, burst_count):
        bullet_width = 16
        rows = 10
        cols = 5
        start_y = self.rect.bottom + 5
        if burst_count < rows:
            y = start_y + burst_count * 15
            start_x = self.rect.left + bullet_width // 2
            end_x = self.rect.right - bullet_width // 2
            step_x = (end_x - start_x) / (cols - 1) if cols > 1 else 0
            for col in range(cols):
                x = start_x + col * step_x
                eb = EnemyBullet(x, y)
                eb.speedy = 7
                eb.speed_x = 0
                all_sprites.add(eb)
                enemy_bullets.add(eb)

    # 模式3：扇形散射 保持原版一次性发射逻辑
    def burst_shoot_mode3(self):
        center_x = self.rect.centerx
        center_y = self.rect.bottom
        bullet_count = 24
        start_angle = 0
        end_angle = math.pi
        speed = 6
        for i in range(bullet_count):
            angle = start_angle + (end_angle - start_angle) * i / (bullet_count - 1)
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            eb = EnemyBullet(center_x, center_y)
            eb.speed_x = dx
            eb.speedy = dy
            all_sprites.add(eb)
            enemy_bullets.add(eb)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0 and not self.explosion_played:
            self.explosion_played = True
            effect = ExplosionEffect(self.rect.centerx, self.rect.centery, explosion_frames)
            all_sprites.add(effect)
            global game_stage, stage_start_time
            game_stage = STAGE_WIN
            stage_start_time = pygame.time.get_ticks()
            self.kill()
            for group in [rocks, enemy1_group, enemy2_group, enemy3_group, enemy4_group,
                          enemy6_group, enemy7_group, enemy8_group, enemy13_group,
                          enemy5_group, enemy9_group, enemy10_group, enemy11_group, enemy12_group,
                          special_enemies, boss_group]:
                for enemy in group:
                    enemy.kill()
            for bullet in enemy_bullets:
                bullet.kill()

    def update(self):
        if self.frozen:
            if pygame.time.get_ticks() >= self.frozen_until:
                self.frozen = False
            else:
                return
        if self.entering:
            self.rect.y += self.enter_speed
            if self.rect.y >= self.enter_target_y:
                self.rect.y = self.enter_target_y
                self.entering = False
                self.next_attack = pygame.time.get_ticks() + self.attack_interval
                self.rect.clamp_ip(self.move_area)
            return
        # 移动逻辑不变
        self.rect.x += self.speed_x
        if self.rect.left < self.move_area.left or self.rect.right > self.move_area.right:
            self.speed_x *= -1
            self.rect.clamp_ip(self.move_area)
        self.rect.y += self.speed_y
        if self.rect.top < self.move_area.top or self.rect.bottom > self.move_area.bottom:
            self.speed_y *= -1
            self.rect.clamp_ip(self.move_area)

        now = pygame.time.get_ticks()
        # 处理分批次攻击（仅模式1、2）
        if self.attack_active:
            if now - self.burst_timer >= self.burst_delay:
                if self.current_attack_mode == 1:
                    self.burst_shoot_mode1(self.burst_count)
                    if self.burst_count >= 1: # 2批打完结束
                        self.attack_active = False
                elif self.current_attack_mode == 2:
                    self.burst_shoot_mode2(self.burst_count)
                    if self.burst_count >= 9: # 10批打完结束
                        self.attack_active = False
                self.burst_count += 1
                self.burst_timer = now
                # 攻击结束切换模式
                if not self.attack_active:
                    self.mode = self.mode % 3 + 1

        # 触发新攻击逻辑
        if not self.attack_active and now >= self.next_attack:
            if self.mode == 3:
                # 模式3直接一次性发射
                self.burst_shoot_mode3()
                self.mode = 1 # 发射完切回模式1
                self.next_attack = now + self.attack_interval
            else:
                # 模式1、2启动分批次发射
                self.attack_active = True
                self.current_attack_mode = self.mode
                self.burst_count = 0
                self.burst_timer = now
                self.next_attack = now + self.attack_interval

    def move_with_bg(self, offset_change):
        pass


class Boss2(EnemyBase):
    def __init__(self):
        super().__init__(BOSS2_HP)
        self.is_boss = True
        boss_scale_h = 345
        boss_scale_w = 300
        self.image = pygame.transform.scale(boss2_img, (boss_scale_w, boss_scale_h))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = min(boss_scale_w, boss_scale_h) // 2
        self.entering = True
        self.enter_speed = 2
        self.enter_target_y = 30
        self.rect.x = WIDTH // 2 - boss_scale_w // 2
        self.rect.y = -boss_scale_h
        self.speed_x = 1.5
        self.speed_y = 1
        self.move_area = pygame.Rect(20, self.enter_target_y, WIDTH - 40, 500)
        self.mode = 1
        self.attack_interval = 3000
        self.next_attack = 0
        self.explosion_played = False
        self.frozen = False
        self.frozen_until = 0

        # 分批次攻击控制
        self.attack_active = False
        self.current_attack_mode = None
        self.burst_count = 0
        self.burst_timer = 0
        self.burst_delay = 150

    # ---------- 攻击1：连续两次扇形散射 ----------
    def burst_shoot_mode1(self, burst_count):
        center_x = self.rect.centerx - 10
        center_y = self.rect.bottom - 100
        bullet_count = 24
        speed = 6
        for i in range(bullet_count):
            angle = (math.pi * i) / (bullet_count - 1)   # 0 到 pi 均匀分布
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            eb = EnemyBullet(center_x, center_y)
            eb.speed_x = dx
            eb.speedy = dy
            all_sprites.add(eb)
            enemy_bullets.add(eb)

    # ---------- 攻击2：12组左右子弹，分批次 ----------
    def burst_shoot_mode2(self, burst_count):
        left_x = self.rect.centerx - 30
        right_x = self.rect.centerx + 30
        y = self.rect.bottom - 30  # 完全由 Boss 当前位置决定

        speed = 5
        if player and not player.dying:
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            dist = math.hypot(dx, dy)
            if dist > 0:
                vx = (dx / dist) * speed
                vy = (dy / dist) * speed
            else:
                vx, vy = 0, speed
        else:
            vx, vy = 0, speed

        bullet_class = EnemyBullet
        left_eb = bullet_class(left_x, y)
        right_eb = bullet_class(right_x, y)
        left_eb.speed_x = vx
        left_eb.speedy = vy
        right_eb.speed_x = vx
        right_eb.speedy = vy
        all_sprites.add(left_eb, right_eb)
        enemy_bullets.add(left_eb, right_eb)

    # ---------- 攻击3：双激光，从飞机上方发射 ----------
    def burst_shoot_mode3(self, burst_count=None):
        # 发射左右两束激光，发射点可调
        laser_left_x = self.rect.centerx - 140
        laser_right_x = self.rect.centerx + 100
        emitter_offset = -190   # 飞机顶部向上10像素开始
        laser_left = BossLaserBeam(laser_left_x, self.rect.top - emitter_offset, self, emitter_offset)
        laser_right = BossLaserBeam(laser_right_x, self.rect.top - emitter_offset, self, emitter_offset)
        all_sprites.add(laser_left, laser_right)
        enemy_bullets.add(laser_left, laser_right)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0 and not self.explosion_played:
            self.explosion_played = True
            effect = ExplosionEffect(self.rect.centerx, self.rect.centery, explosion_frames)
            all_sprites.add(effect)
            global game_stage, stage_start_time
            game_stage = STAGE_WIN
            stage_start_time = pygame.time.get_ticks()
            self.kill()
            for group in [rocks, enemy1_group, enemy2_group, enemy3_group, enemy4_group,
                          enemy6_group, enemy7_group, enemy8_group, enemy13_group,
                          enemy5_group, enemy9_group, enemy10_group, enemy11_group, enemy12_group,
                          special_enemies, boss_group]:
                for enemy in group:
                    enemy.kill()
            for bullet in enemy_bullets:
                bullet.kill()

    def update(self):
        if self.frozen:
            if pygame.time.get_ticks() >= self.frozen_until:
                self.frozen = False
            else:
                return
        if self.entering:
            self.rect.y += self.enter_speed
            if self.rect.y >= self.enter_target_y:
                self.rect.y = self.enter_target_y
                self.entering = False
                self.next_attack = pygame.time.get_ticks() + self.attack_interval
                self.rect.clamp_ip(self.move_area)
            return

        # 移动
        self.rect.x += self.speed_x
        if self.rect.left < self.move_area.left or self.rect.right > self.move_area.right:
            self.speed_x *= -1
            self.rect.clamp_ip(self.move_area)
        self.rect.y += self.speed_y
        if self.rect.top < self.move_area.top or self.rect.bottom > self.move_area.bottom:
            self.speed_y *= -1
            self.rect.clamp_ip(self.move_area)

        now = pygame.time.get_ticks()

        # 处理分批次攻击（模式1、2）
        if self.attack_active:
            if now - self.burst_timer >= self.burst_delay:
                if self.current_attack_mode == 1:
                    # 模式1：两次扇形
                    self.burst_shoot_mode1(self.burst_count)
                    if self.burst_count >= 1:   # 0和1共两次
                        self.attack_active = False
                elif self.current_attack_mode == 2:
                    # 模式2：12组，burst_count 0~11
                    self.burst_shoot_mode2(self.burst_count)
                    if self.burst_count >= 11:  # 12组打完
                        self.attack_active = False

                self.burst_count += 1
                self.burst_timer = now

                if not self.attack_active:
                    self.mode = self.mode % 3 + 1

        # 触发新攻击
        if not self.attack_active and now >= self.next_attack:
            if self.mode == 3:
                # 模式3：激光，直接发射，不进入批次循环
                self.burst_shoot_mode3()
                self.mode = 1
                self.next_attack = now + self.attack_interval
            else:
                self.attack_active = True
                self.current_attack_mode = self.mode
                self.burst_count = 0
                self.burst_timer = now
                self.next_attack = now + self.attack_interval

    def move_with_bg(self, offset_change):
        pass


class Boss3(EnemyBase):
    def __init__(self):
        super().__init__(15000)          # 第三关 Boss 血量
        self.is_boss = True
        boss_scale_h = 357               # 根据图片可调
        boss_scale_w = 289
        self.image = pygame.transform.scale(boss3_img, (boss_scale_w, boss_scale_h))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = min(boss_scale_w, boss_scale_h) // 2
        self.entering = True
        self.enter_speed = 2
        self.enter_target_y = 30
        self.rect.x = WIDTH // 2 - boss_scale_w // 2
        self.rect.y = -boss_scale_h
        self.speed_x = 1.5
        self.speed_y = 1
        self.move_area = pygame.Rect(20, self.enter_target_y, WIDTH - 40, 450)  # 高度给足
        self.mode = 1
        self.attack_interval = 3000
        self.next_attack = 0
        self.explosion_played = False
        self.frozen = False
        self.frozen_until = 0

        # 分批次攻击控制
        self.attack_active = False
        self.current_attack_mode = None
        self.burst_count = 0
        self.burst_timer = 0
        self.burst_delay = 150

        # ----- 可独立调节的三束激光发射器位置（全部从飞机上方射出）-----
        # 左激光
        self.laser_left_offset_x = -138  # 水平偏移（负值为左侧）
        self.laser_left_offset_y = -130  # 垂直偏移（正值为飞机顶部向上像素）
        # 中激光
        self.laser_mid_offset_x = -23
        self.laser_mid_offset_y = -260
        # 右激光
        self.laser_right_offset_x = 95
        self.laser_right_offset_y = -130

    # ---------- 攻击1：连续三次扇形散射 ----------
    def burst_shoot_mode1(self, burst_count):
        # 发射 24 发扇形子弹（0 到 π），共 3 批
        center_x = self.rect.centerx
        center_y = self.rect.bottom - 30
        bullet_count = 24
        speed = 6
        for i in range(bullet_count):
            angle = (math.pi * i) / (bullet_count - 1)
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            eb = EnemyBullet(center_x, center_y)
            eb.speed_x = dx
            eb.speedy = dy
            all_sprites.add(eb)
            enemy_bullets.add(eb)

    # ---------- 攻击2：12组左右子弹，朝向玩家 ----------
    def burst_shoot_mode2(self, burst_count):
        # 左右两颗并排，间隔可调
        left_x = self.rect.centerx - 30
        right_x = self.rect.centerx + 30
        # 子弹起始Y坐标，从机身底部向上偏移避免虚空出现
        y = self.rect.bottom - 30

        # 计算指向玩家的方向
        if player and not player.dying:
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            dist = math.hypot(dx, dy)
            if dist > 0:
                speed = 5
                vx = (dx / dist) * speed
                vy = (dy / dist) * speed
            else:
                vx, vy = 0, 5
        else:
            vx, vy = 0, 5

        # 使用普通敌机子弹
        bullet_class = EnemyBullet

        left_eb = bullet_class(left_x, y)
        right_eb = bullet_class(right_x, y)
        left_eb.speed_x = vx
        left_eb.speedy = vy
        right_eb.speed_x = vx
        right_eb.speedy = vy
        all_sprites.add(left_eb, right_eb)
        enemy_bullets.add(left_eb, right_eb)

    # ---------- 攻击3：三激光（左右上方 + 中间下方） ----------
    def burst_shoot_mode3(self, burst_count=None):
        # 左激光
        left_x = self.rect.centerx + self.laser_left_offset_x
        left_y_offset = self.laser_left_offset_y
        laser_left = BossLaserBeam(left_x, self.rect.top - left_y_offset, self, left_y_offset)

        # 中激光
        mid_x = self.rect.centerx + self.laser_mid_offset_x
        mid_y_offset = self.laser_mid_offset_y
        laser_mid = BossLaserBeam(mid_x, self.rect.top - mid_y_offset, self, mid_y_offset)

        # 右激光
        right_x = self.rect.centerx + self.laser_right_offset_x
        right_y_offset = self.laser_right_offset_y
        laser_right = BossLaserBeam(right_x, self.rect.top - right_y_offset, self, right_y_offset)

        all_sprites.add(laser_left, laser_mid, laser_right)
        enemy_bullets.add(laser_left, laser_mid, laser_right)

    # ---------- 死亡处理（同 Boss1/2）----------
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0 and not self.explosion_played:
            self.explosion_played = True
            effect = ExplosionEffect(self.rect.centerx, self.rect.centery, explosion_frames)
            all_sprites.add(effect)
            global game_stage, stage_start_time
            game_stage = STAGE_WIN
            stage_start_time = pygame.time.get_ticks()
            self.kill()
            for group in [rocks, enemy1_group, enemy2_group, enemy3_group, enemy4_group,
                          enemy6_group, enemy7_group, enemy8_group, enemy13_group,
                          enemy5_group, enemy9_group, enemy10_group, enemy11_group, enemy12_group,
                          special_enemies, boss_group]:
                for enemy in group:
                    enemy.kill()
            for bullet in enemy_bullets:
                bullet.kill()

    def update(self):
        if self.frozen:
            if pygame.time.get_ticks() >= self.frozen_until:
                self.frozen = False
            else:
                return

        if self.entering:
            self.rect.y += self.enter_speed
            if self.rect.y >= self.enter_target_y:
                self.rect.y = self.enter_target_y
                self.entering = False
                self.next_attack = pygame.time.get_ticks() + self.attack_interval
                self.rect.clamp_ip(self.move_area)
            return

        # 移动
        self.rect.x += self.speed_x
        if self.rect.left < self.move_area.left or self.rect.right > self.move_area.right:
            self.speed_x *= -1
            self.rect.clamp_ip(self.move_area)
        self.rect.y += self.speed_y
        if self.rect.top < self.move_area.top or self.rect.bottom > self.move_area.bottom:
            self.speed_y *= -1
            self.rect.clamp_ip(self.move_area)

        now = pygame.time.get_ticks()

        # 处理分批次攻击（模式1、2）
        if self.attack_active:
            if now - self.burst_timer >= self.burst_delay:
                if self.current_attack_mode == 1:
                    self.burst_shoot_mode1(self.burst_count)
                    if self.burst_count >= 4:  # 0,1,2 共3次扇形
                        self.attack_active = False
                elif self.current_attack_mode == 2:
                    self.burst_shoot_mode2(self.burst_count)
                    if self.burst_count >= 23:  # 0~5 共6组
                        self.attack_active = False
                self.burst_count += 1
                self.burst_timer = now
                if not self.attack_active:
                    self.mode = self.mode % 3 + 1  # 切换到下一个模式

        # 触发新攻击
        if not self.attack_active and now >= self.next_attack:
            if self.mode == 3:
                self.burst_shoot_mode3()
                self.mode = 1
                self.next_attack = now + self.attack_interval
            else:
                self.attack_active = True
                self.current_attack_mode = self.mode
                self.burst_count = 0
                self.burst_timer = now
                self.next_attack = now + self.attack_interval

    def move_with_bg(self, offset_change):
        pass


class Boss4(EnemyBase):
    def __init__(self):
        super().__init__(BOSS4_HP)
        self.is_boss = True
        boss_scale_h = 350          # 根据实际图片调整
        boss_scale_w = 350
        # 如有专门的boss4图片，请替换；这里暂用boss3图片示意
        self.image = pygame.transform.scale(boss4_img, (boss_scale_w, boss_scale_h))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 120
        self.entering = True
        self.enter_speed = 2
        self.enter_target_y = 30
        self.rect.x = WIDTH // 2 - boss_scale_w // 2
        self.rect.y = -boss_scale_h
        self.speed_x = 1.5
        self.speed_y = 1
        self.move_area = pygame.Rect(20, self.enter_target_y, WIDTH - 40, 450)

        self.mode = 1
        self.attack_interval = 1500
        self.next_attack = 0
        self.explosion_played = False
        self.frozen = False
        self.frozen_until = 0

        # 分批次攻击控制
        self.attack_active = False
        self.current_attack_mode = None
        self.burst_count = 0
        self.burst_timer = 0
        self.burst_delay = 150

        # 攻击1：左右扇形发射位置偏移
        self.atk1_left_offset = (-80, -150)   # (x偏移, y偏移)
        self.atk1_right_offset = (70, -150)

        # 攻击2：四发射点的水平偏移
        self.atk2_offsets = [
            -40,   # 左
            0,   # 中下
            0,    # 中上
            40     # 右
        ]
        self.atk2_y_variation = 10

        # 攻击3：三激光偏移
        self.laser_left_offset = (-110, -130)
        self.laser_mid_offset = (-20, -260)
        self.laser_right_offset = (75, -130)

        # 攻击4：俯冲状态
        self.diving = False
        self.rising = False
        self.dive_speed = 8
        self.rise_speed = 4
        self.dive_target_y = HEIGHT - 10    # 快到底部
        self.rise_target_y = self.enter_target_y  # 回到进入后的高度
        self.attack4_active = False

        # 攻击5：召唤敌机循环
        self.summon_cycle = [
            ('enemy6', 4),
            ('enemy8', 8),
            ('enemy11', 2),
            ('enemy12', 1),
            ('enemy13', 6)
        ]
        self.summon_index = 0          # 当前召唤类型索引
        self.summon_count = 0          # 该类型已召唤数量
        self.summon_timer = 0
        self.summon_delay = 300        # 每个敌机召唤间隔
        self.summon_active = False

        self.debug_show_hitbox = True  # 设为 False 可关闭调试绘制

    # ---------- 攻击1：连续4次左右圆形弹幕 ----------
    def burst_shoot_mode1(self, burst_count):
        # 左右两个发射点（位置可调）
        left_x = self.rect.centerx + self.atk1_left_offset[0]
        left_y = self.rect.centery + self.atk1_left_offset[1]
        right_x = self.rect.centerx + self.atk1_right_offset[0]
        right_y = self.rect.centery + self.atk1_right_offset[1]

        bullet_count = 16  # 每个圆圈的子弹数（可调）
        speed = 5  # 子弹速度（可调）

        # 左侧发射完整一圈
        for i in range(bullet_count):
            angle = math.radians(i * (360 / bullet_count))
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            eb = EnemyBullet(left_x, left_y)
            eb.speed_x = dx
            eb.speedy = dy
            all_sprites.add(eb)
            enemy_bullets.add(eb)

        # 右侧发射完整一圈
        for i in range(bullet_count):
            angle = math.radians(i * (360 / bullet_count))
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            eb = EnemyBullet(right_x, right_y)
            eb.speed_x = dx
            eb.speedy = dy
            all_sprites.add(eb)
            enemy_bullets.add(eb)

    # ---------- 攻击2：12组4颗朝向玩家的子弹 ----------
    def burst_shoot_mode2(self, burst_count):
        # 计算朝向玩家的速度
        if player and not player.dying:
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            dist = math.hypot(dx, dy)
            speed = 5
            if dist > 0:
                vx = (dx / dist) * speed
                vy = (dy / dist) * speed
            else:
                vx, vy = 0, speed
        else:
            vx, vy = 0, 5

        base_y = self.rect.bottom - 30
        # 四个发射点：左、中下(偏移-y)、中上(偏移+y)、右
        points = [
            (self.rect.centerx + self.atk2_offsets[0], base_y),
            (self.rect.centerx + self.atk2_offsets[1], base_y + self.atk2_y_variation),
            (self.rect.centerx + self.atk2_offsets[2], base_y - self.atk2_y_variation),
            (self.rect.centerx + self.atk2_offsets[3], base_y)
        ]
        for x, y in points:
            eb = EnemyBullet(x, y)
            eb.speed_x = vx
            eb.speedy = vy
            all_sprites.add(eb)
            enemy_bullets.add(eb)

    # ---------- 攻击3：三激光 ----------
    def burst_shoot_mode3(self, burst_count=None):
        left_x = self.rect.centerx + self.laser_left_offset[0]
        left_y_off = self.laser_left_offset[1]
        laser_left = BossLaserBeam(left_x, self.rect.top - left_y_off, self, left_y_off)

        mid_x = self.rect.centerx + self.laser_mid_offset[0]
        mid_y_off = self.laser_mid_offset[1]
        laser_mid = BossLaserBeam(mid_x, self.rect.top - mid_y_off, self, mid_y_off)

        right_x = self.rect.centerx + self.laser_right_offset[0]
        right_y_off = self.laser_right_offset[1]
        laser_right = BossLaserBeam(right_x, self.rect.top - right_y_off, self, right_y_off)

        all_sprites.add(laser_left, laser_mid, laser_right)
        enemy_bullets.add(laser_left, laser_mid, laser_right)

    # ---------- 攻击4：俯冲与回升 ----------
    def start_attack4(self):
        self.attack4_active = True
        self.diving = True
        self.rising = False
        self.dive_target_y = HEIGHT - 50
        self.rise_target_y = self.enter_target_y

    def update_attack4(self):
        if self.diving:
            self.rect.y += self.dive_speed
            if self.rect.bottom >= self.dive_target_y:
                self.rect.bottom = self.dive_target_y
                self.diving = False
                self.rising = True
        elif self.rising:
            self.rect.y -= self.rise_speed
            if self.rect.top <= self.rise_target_y:
                self.rect.top = self.rise_target_y
                self.rising = False
                self.attack4_active = False
                # 攻击4结束，切换到下一个模式（5）
                self.mode = self.mode % 5 + 1
                self.next_attack = pygame.time.get_ticks() + self.attack_interval

    def start_attack5(self):
        if not self.summon_active:
            self.summon_active = True
            enemy_type, total = self.summon_cycle[self.summon_index]
            self.summon_count = 0
            self.summon_total = total
            self.summon_timer = 0
            self.summon_enemy_type = enemy_type

    # ---------- 攻击5：召唤敌机 ----------
    def update_attack5(self):
        if not self.summon_active:
            return
        now = pygame.time.get_ticks()
        if now - self.summon_timer >= self.summon_delay:
            self.summon_timer = now
            # 生成敌机的位置：Boss 底部（从下方“喷出”）
            spawn_x = self.rect.centerx
            spawn_y = self.rect.bottom  # 或者 self.rect.centery

            if self.summon_enemy_type == 'enemy6':
                e = Enemy6(spawn_x)
            elif self.summon_enemy_type == 'enemy8':
                e = Enemy8(spawn_x)
            elif self.summon_enemy_type == 'enemy11':
                e = Enemy11(spawn_x)
            elif self.summon_enemy_type == 'enemy12':
                e = Enemy12(spawn_x)
            elif self.summon_enemy_type == 'enemy13':
                e = Enemy13(spawn_x)
            else:
                return

            # 设置生成位置（覆盖敌机原本的 y 坐标）
            e.rect.centerx = spawn_x
            e.rect.bottom = spawn_y  # 让底部对齐 Boss 底部，也可以设 e.rect.centery = spawn_y

            # 加入精灵组
            all_sprites.add(e)
            # 根据类型加入对应小组
            if self.summon_enemy_type == 'enemy6':
                enemy6_group.add(e)
            elif self.summon_enemy_type == 'enemy8':
                enemy8_group.add(e)
            elif self.summon_enemy_type == 'enemy11':
                enemy11_group.add(e)
            elif self.summon_enemy_type == 'enemy12':
                enemy12_group.add(e)
            elif self.summon_enemy_type == 'enemy13':
                enemy13_group.add(e)

            self.summon_count += 1
            if self.summon_count >= self.summon_total:
                self.summon_index = (self.summon_index + 1) % len(self.summon_cycle)
                self.summon_active = False

    # ---------- 死亡处理（与 Boss1/2/3 类似）----------
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0 and not self.explosion_played:
            self.explosion_played = True
            effect = ExplosionEffect(self.rect.centerx, self.rect.centery, explosion_frames)
            all_sprites.add(effect)
            self.kill()
            # 清除所有敌人和子弹
            for group in [rocks, enemy1_group, enemy2_group, enemy3_group, enemy4_group,
                          enemy6_group, enemy7_group, enemy8_group, enemy13_group,
                          enemy5_group, enemy9_group, enemy10_group, enemy11_group, enemy12_group,
                          special_enemies, boss_group]:
                for enemy in group:
                    enemy.kill()
            for bullet in enemy_bullets:
                bullet.kill()
            # 切换为最终胜利状态
            global game_state, final_win_text_index, final_win_last_update
            game_state = STATE_FINAL_WIN
            final_win_text_index = 0
            final_win_last_update = pygame.time.get_ticks()

    def update(self):
        if self.frozen:
            if pygame.time.get_ticks() >= self.frozen_until:
                self.frozen = False
            else:
                return

        if self.entering:
            self.rect.y += self.enter_speed
            if self.rect.y >= self.enter_target_y:
                self.rect.y = self.enter_target_y
                self.entering = False
                self.next_attack = pygame.time.get_ticks() + self.attack_interval
                self.rect.clamp_ip(self.move_area)
            return

        # 如果正在进行攻击4，仅处理俯冲逻辑，暂停其他攻击
        if self.attack4_active:
            self.update_attack4()
            if not self.attack4_active:
                # 攻击4结束，恢复普通移动并设置下次攻击
                self.next_attack = pygame.time.get_ticks() + self.attack_interval
            return

        # 普通移动
        self.rect.x += self.speed_x
        if self.rect.left < self.move_area.left or self.rect.right > self.move_area.right:
            self.speed_x *= -1
            self.rect.clamp_ip(self.move_area)
        self.rect.y += self.speed_y
        if self.rect.top < self.move_area.top or self.rect.bottom > self.move_area.bottom:
            self.speed_y *= -1
            self.rect.clamp_ip(self.move_area)

        now = pygame.time.get_ticks()

        # 处理攻击5的召唤逻辑（独立于批次攻击）
        if self.summon_active:
            self.update_attack5()
            if not self.summon_active:
                self.mode = self.mode % 5 + 1
                self.next_attack = now + self.attack_interval
            return  # 召唤期间不处理其他攻击

        # 处理分批次攻击（模式1、2）
        if self.attack_active:
            if now - self.burst_timer >= self.burst_delay:
                if self.current_attack_mode == 1:
                    self.burst_shoot_mode1(self.burst_count)
                    if self.burst_count >= 3:   # 4次：0,1,2,3
                        self.attack_active = False
                elif self.current_attack_mode == 2:
                    self.burst_shoot_mode2(self.burst_count)
                    if self.burst_count >= 11:  # 12组：0~11
                        self.attack_active = False
                self.burst_count += 1
                self.burst_timer = now
                if not self.attack_active:
                    self.mode = self.mode % 5 + 1

        # 触发新攻击
        if not self.attack_active and not self.summon_active and not self.attack4_active and now >= self.next_attack:
            if self.mode == 3:
                # 攻击3：激光，直接发射
                self.burst_shoot_mode3()
                self.mode = self.mode % 5 + 1
                self.next_attack = now + self.attack_interval
            elif self.mode == 4:
                # 攻击4：俯冲
                self.start_attack4()
                # 攻击4由自己的计时器控制，不重置next_attack，待其结束后再恢复
                # 这里直接进入攻击4状态，不设置mode切换，结束后恢复
            elif self.mode == 5:
                # 攻击5：召唤
                self.start_attack5()
                # 同理，由召唤逻辑结束后切换mode
            else:
                self.attack_active = True
                self.current_attack_mode = self.mode
                self.burst_count = 0
                self.burst_timer = now
                self.next_attack = now + self.attack_interval

    def move_with_bg(self, offset_change):
        pass


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, type='yellow', color_cycle=False):
        super().__init__()
        self.type = type
        self.color_cycle = color_cycle
        self.current_color = type
        self.create_time = pygame.time.get_ticks()
        self.speedy = 0.45
        self.color_images = {
            'yellow': pygame.transform.scale(powerup_img, (50, 50)),
            'blue': pygame.transform.scale(powerup_blue_img, (50, 50)),
            'red': pygame.transform.scale(powerup_red_img, (50, 50))
        }
        if type == 'ultimate':
            self.orig_image = ultimate_ball_img.copy()
        else:
            self.orig_image = self.color_images.get(type, self.color_images['yellow'])
            self.orig_image.set_colorkey(BLACK)
        self.image = self.orig_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.y = float(self.rect.y)

    def update_image(self):
        if self.type == 'ultimate':
            return
        img = self.color_images.get(self.current_color, self.color_images['yellow'])
        self.orig_image = img.copy()
        self.orig_image.set_colorkey(BLACK)
        self.image = self.orig_image.copy()

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def update(self):
        self.y += self.speedy
        self.rect.y = int(self.y)
        if self.rect.top > HEIGHT:
            self.kill()
            return
        color_order = ['yellow', 'blue', 'red']
        if self.color_cycle and self.type != 'ultimate':
            now = pygame.time.get_ticks()
            elapsed = now - self.create_time
            cycle = (elapsed // 10000) % 3
            start_idx = color_order.index(self.type)
            new_color = color_order[(start_idx + cycle) % 3]
            if new_color != self.current_color:
                self.current_color = new_color
                self.update_image()
                self.rect = self.image.get_rect(center=self.rect.center)
                self.y = float(self.rect.y)
        now = pygame.time.get_ticks()
        period = 800
        t = (now - self.create_time) % period / period
        alpha = int(80 + 175 * (math.sin(t * 2 * math.pi) * 0.5 + 0.5))
        self.image = self.orig_image.copy()
        self.image.set_alpha(alpha)


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(enemy_bullet_img, (16, 16))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 6
        self.rect.centerx = x
        self.rect.top = y
        self.speedy = 7
        self.speed_x = 0
        self.damage = 20

    def move_with_bg(self, offset_change):
        self.rect.x += offset_change

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speed_x
        if self.rect.top > HEIGHT or self.rect.bottom < 0 or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()


class EnemyBullet2(EnemyBullet):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speedy = 5
        self.image = enemy_bullet2_img.copy()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = 5
        self.damage = 50


class NukeBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(NukeBullet_img, (12, 35))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(x, y))
        self.speedy = -10
        self.damage = 1000
        self.explosion_radius = 250

    def update(self):
        self.rect.y += self.speedy
        hit_enemy = pygame.sprite.spritecollideany(self, rocks) or \
                    pygame.sprite.spritecollideany(self, enemy1_group) or \
                    pygame.sprite.spritecollideany(self, enemy2_group) or \
                    pygame.sprite.spritecollideany(self, enemy3_group) or \
                    pygame.sprite.spritecollideany(self, enemy4_group) or \
                    pygame.sprite.spritecollideany(self, enemy6_group) or \
                    pygame.sprite.spritecollideany(self, enemy7_group) or \
                    pygame.sprite.spritecollideany(self, enemy8_group) or \
                    pygame.sprite.spritecollideany(self, enemy13_group) or \
                    pygame.sprite.spritecollideany(self, enemy5_group) or \
                    pygame.sprite.spritecollideany(self, enemy9_group) or \
                    pygame.sprite.spritecollideany(self, enemy10_group) or \
                    pygame.sprite.spritecollideany(self, enemy11_group) or \
                    pygame.sprite.spritecollideany(self, enemy12_group) or \
                    pygame.sprite.spritecollideany(self, boss_group) or \
                    pygame.sprite.spritecollideany(self, special_enemies)
        if self.rect.centery <= HEIGHT // 3 or hit_enemy:
            self.explode()
            self.kill()

    def explode(self):
        for bullet in list(enemy_bullets):
            if math.hypot(bullet.rect.centerx - self.rect.centerx,
                          bullet.rect.centery - self.rect.centery) < self.explosion_radius:
                bullet.kill()
        all_enemies = (rocks.sprites() + enemy1_group.sprites() + enemy2_group.sprites() +
                       enemy3_group.sprites() + enemy4_group.sprites() + enemy6_group.sprites() +
                       enemy7_group.sprites() + enemy8_group.sprites() + enemy13_group.sprites() +
                       enemy5_group.sprites() + enemy9_group.sprites() + enemy10_group.sprites() +
                       enemy11_group.sprites() + enemy12_group.sprites() +
                       boss_group.sprites() + special_enemies.sprites())
        for enemy in all_enemies:
            dx = enemy.rect.centerx - self.rect.centerx
            dy = enemy.rect.centery - self.rect.centery
            if math.hypot(dx, dy) < self.explosion_radius:
                enemy.take_damage(self.damage)
        effect = ExplosionEffect(self.rect.centerx, self.rect.centery, explosion_frames)
        all_sprites.add(effect)


class ExplosionEffect(pygame.sprite.Sprite):
    def __init__(self, x, y, frames):
        super().__init__()
        self.frames = frames
        self.frame_index = 0
        self.frame_duration = 60
        self.last_update = pygame.time.get_ticks()
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_index]
                self.rect = self.image.get_rect(center=self.rect.center)


class PlayerExplosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = player_explosion_frames
        self.frame_index = 0
        self.frame_duration = 60
        self.last_update = pygame.time.get_ticks()
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_index]
                self.rect = self.image.get_rect(center=self.rect.center)


class HitExplosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = hit_explode_frames
        self.frame_index = 0
        self.frame_duration = 60
        self.last_update = pygame.time.get_ticks()
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_index]
                self.rect = self.image.get_rect(center=self.rect.center)


class EnemyExplosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = enemy_explode_frames
        self.frame_index = 0
        self.frame_duration = 60
        self.last_update = pygame.time.get_ticks()
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_index]
                self.rect = self.image.get_rect(center=self.rect.center)


class HomingMissile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = missile_track_img.copy()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7
        self.speed_x = 0
        self.speed_y = -self.speed
        self.damage = 50

    def update(self):
        target = None
        min_dist = float('inf')
        all_enemies = (rocks.sprites() + enemy1_group.sprites() + enemy2_group.sprites() +
                       enemy3_group.sprites() + enemy4_group.sprites() + enemy6_group.sprites() +
                       enemy7_group.sprites() + enemy8_group.sprites() + enemy13_group.sprites() +
                       enemy5_group.sprites() + enemy9_group.sprites() + enemy10_group.sprites() +
                       enemy11_group.sprites() + enemy12_group.sprites() +
                       special_enemies.sprites() + boss_group.sprites())
        for e in all_enemies:
            if not e.alive():
                continue
            dx = e.rect.centerx - self.rect.centerx
            dy = e.rect.centery - self.rect.centery
            dist = math.hypot(dx, dy)
            if dist < min_dist:
                min_dist = dist
                target = e
        if target is not None:
            dx = target.rect.centerx - self.rect.centerx
            dy = target.rect.centery - self.rect.centery
            dist = math.hypot(dx, dy)
            if dist != 0:
                self.speed_x = (dx / dist) * self.speed
                self.speed_y = (dy / dist) * self.speed
        else:
            self.speed_x = 0
            self.speed_y = -self.speed
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        for e in all_enemies:
            if self.rect.colliderect(e.rect):
                e.take_damage(self.damage)
                hit_effect = HitExplosion(e.rect.centerx, e.rect.centery)
                all_sprites.add(hit_effect)
                self.kill()
                return
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.left < 0 or self.rect.right > WIDTH:
            self.kill()


class Wormhole(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.orig_image = wormhole_img.copy()
        self.image = self.orig_image.copy()
        self.rect = self.image.get_rect()
        self.duration = 3000
        self.anim_in = 500
        self.anim_out = 500
        self.born_time = pygame.time.get_ticks()
        self.min_scale = 0.2
        self.max_scale = 1.0

    def update(self):
        now = pygame.time.get_ticks()
        elapsed = now - self.born_time
        if elapsed < self.anim_in:
            progress = elapsed / self.anim_in
            scale = self.min_scale + (self.max_scale - self.min_scale) * progress
        elif elapsed > self.duration - self.anim_out:
            remaining = self.duration - elapsed
            if remaining < 0:
                remaining = 0
            progress = remaining / self.anim_out
            scale = self.min_scale + (self.max_scale - self.min_scale) * progress
        else:
            scale = self.max_scale
        size = int(self.orig_image.get_width() * scale), int(self.orig_image.get_height() * scale)
        self.image = pygame.transform.scale(self.orig_image, size)
        self.rect = self.image.get_rect(
            center=(self.player.rect.centerx, self.player.rect.top - self.image.get_height() // 2))
        if elapsed >= self.duration:
            self.player.ultimate_active = False
            self.kill()
            return
        all_enemies = (rocks.sprites() + enemy1_group.sprites() + enemy2_group.sprites() +
                       enemy3_group.sprites() + enemy4_group.sprites() + enemy6_group.sprites() +
                       enemy7_group.sprites() + enemy8_group.sprites() + enemy13_group.sprites() +
                       enemy5_group.sprites() + enemy9_group.sprites() + enemy10_group.sprites() +
                       enemy11_group.sprites() + enemy12_group.sprites() +
                       special_enemies.sprites() + boss_group.sprites())
        for e in all_enemies:
            if self.rect.colliderect(e.rect):
                if e.is_boss:
                    if not e.frozen:
                        e.frozen = True
                        e.frozen_until = now + (self.duration - elapsed)
                else:
                    e.kill()
        for bullet in list(enemy_bullets):
            if self.rect.colliderect(bullet.rect):
                bullet.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_ori = pygame.transform.scale(player1_img, (50, 64))
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 6
        self.speedy = 5
        self.weapon_type = 'yellow'
        self.weapon_level_yellow = 0
        self.weapon_level_blue = 0
        self.weapon_level_red = 0
        self.max_hp = PLAYER_MAX_HP
        self.max_bottom = HEIGHT - 35  # 留出 LEVEL 文字的位置（文字在 y = HEIGHT-25，多留点间距）
        self.hp = self.max_hp
        self.lives = PLAYER_LIVES
        self.invincible = False
        self.invincible_end_time = 0
        self.dying = False
        self.ult_charges = PLAYER_ULT_CHARGES
        self.laser_shot_timer = 0
        self.ultimate_active = False
        self.ultimate_preparing = False
        self.ultimate_beam_active = False
        self.ultimate_timer = 0
        self.ultimate_animation_frame = 0
        self.ultimate_last_update = 0
        self.ultimate_beam = None
        self.red_last_shoot = 0
        self.red_shoot_cooldown = 300
        self.missile_last_shoot = 0
        self.missile_cooldown = 650

    def take_damage(self, amount, direct_kill=False):
        if self.invincible or self.dying or self.ultimate_active:
            return
        if direct_kill:
            self.hp = 0
        else:
            self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        self.dying = True
        explosion = PlayerExplosion(self.rect.centerx, self.rect.centery)
        all_sprites.add(explosion)
        self.kill()

    def respawn(self):
        if self.lives > 0:
            self.lives -= 1
            self.hp = self.max_hp
            if self.weapon_type == 'yellow':
                self.weapon_level_yellow = max(0, self.weapon_level_yellow - 2)
            elif self.weapon_type == 'blue':
                self.weapon_level_blue = max(0, self.weapon_level_blue - 2)
                if self.weapon_level_blue == 0:
                    self.weapon_type = 'yellow'
                    self.weapon_level_yellow = 0
            elif self.weapon_type == 'red':
                self.weapon_level_red = max(0, self.weapon_level_red - 2)
                if self.weapon_level_red == 0:
                    self.weapon_type = 'yellow'
                    self.weapon_level_yellow = 0
            self.dying = False
            self.invincible = True
            self.invincible_end_time = pygame.time.get_ticks() + INVINCIBLE_DURATION
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            all_sprites.add(self)
            return True
        else:
            self.dying = False
            global game_over, game_over_start
            game_over = True
            game_over_start = pygame.time.get_ticks()
            return False

    def update(self):
        if self.dying:
            return
        key_passed = pygame.key.get_pressed()
        if key_passed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_passed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if key_passed[pygame.K_UP]:
            self.rect.y -= self.speedy
        if key_passed[pygame.K_DOWN]:
            self.rect.y += self.speedy
        self.rect.clamp_ip(screen.get_rect())
        if self.rect.bottom > self.max_bottom:
            self.rect.bottom = self.max_bottom
        now = pygame.time.get_ticks()
        if self.ultimate_active:
            if self.weapon_type == 'red':
                return
            if self.ultimate_preparing:
                elapsed = now - self.ultimate_timer
                if elapsed >= 2000:
                    self.ultimate_preparing = False
                    self.ultimate_beam_active = True
                    self.ultimate_timer = now
                    old_bottom = self.rect.bottom
                    old_centerx = self.rect.centerx
                    self.image = self.image_ori.copy()
                    self.rect = self.image.get_rect()
                    self.rect.centerx = old_centerx
                    self.rect.bottom = old_bottom
                    beam_width = 150
                    beam_height = max(1, self.rect.top)
                    super_laser = SuperLaserBeam(self.rect.centerx, self.rect.top, beam_width, beam_height,
                                                 laser_frames, self)
                    all_sprites.add(super_laser)
                    bullets.add(super_laser)
                    self.ultimate_beam = super_laser
                else:
                    if now - self.ultimate_last_update > 100:
                        self.ultimate_last_update = now
                        self.ultimate_animation_frame = (self.ultimate_animation_frame + 1) % len(player_laser_frames)
                        laser_img = player_laser_frames[self.ultimate_animation_frame]
                        OVERLAP = 10
                        plane_img = self.image_ori
                        combo_width = max(plane_img.get_width(), laser_img.get_width())
                        combo_height = plane_img.get_height() + OVERLAP
                        combo_surf = pygame.Surface((combo_width, combo_height), pygame.SRCALPHA)
                        plane_x = (combo_width - plane_img.get_width()) // 2
                        plane_y = OVERLAP
                        combo_surf.blit(plane_img, (plane_x, plane_y))
                        laser_x = (combo_width - laser_img.get_width()) // 2
                        combo_surf.blit(laser_img, (laser_x, 0))
                        old_bottom = self.rect.bottom
                        old_centerx = self.rect.centerx
                        self.image = combo_surf
                        self.rect = self.image.get_rect()
                        self.rect.centerx = old_centerx
                        self.rect.bottom = old_bottom
            elif self.ultimate_beam_active:
                if self.ultimate_beam is None or not self.ultimate_beam.alive():
                    self.ultimate_active = False
                    self.ultimate_beam_active = False
                    old_bottom = self.rect.bottom
                    old_centerx = self.rect.centerx
                    self.image = self.image_ori.copy()
                    self.rect = self.image.get_rect()
                    self.rect.centerx = old_centerx
                    self.rect.bottom = old_bottom
        else:
            if self.invincible:
                if now >= self.invincible_end_time:
                    self.invincible = False
                    self.image = self.image_ori.copy()
                else:
                    if (now // 200) % 2 == 0:
                        self.image = self.image_ori.copy()
                    else:
                        self.image = self.image_ori.copy()
                        self.image.set_alpha(64)
            else:
                self.image = self.image_ori.copy()

    def shoot(self):
        if self.ultimate_active:
            return
        if self.weapon_type == 'red':
            now = pygame.time.get_ticks()
            if now - self.red_last_shoot >= self.red_shoot_cooldown:
                self.shoot_red()
                self.red_last_shoot = now
        elif self.weapon_type == 'yellow':
            self.shoot_yellow()
        elif self.weapon_type == 'blue':
            self.shoot_blue()

    def shoot_yellow(self):
        lvl = self.weapon_level_yellow
        cx, top = self.rect.centerx, self.rect.top + 30
        if lvl == 0:
            Bullet(cx + 2, top, damage=20, bullet_type='yellow_main')
        elif lvl == 1:
            Bullet(cx - 14, top, damage=15, bullet_type='yellow_main')
            Bullet(cx + 16, top, damage=15, bullet_type='yellow_main')
        elif lvl == 2:
            Bullet(cx - 19, top, damage=15, bullet_type='yellow_main')
            Bullet(cx - 7, top, damage=8, bullet_type='yellow_small')
            Bullet(cx + 6, top, damage=8, bullet_type='yellow_small')
            Bullet(cx + 21, top, damage=15, bullet_type='yellow_main')
        elif lvl == 3:
            Bullet(cx - 20, top, damage=15, bullet_type='yellow_main')
            Bullet(cx - 8, top, damage=10, bullet_type='yellow_small')
            Bullet(cx + 5, top, damage=10, bullet_type='yellow_small')
            Bullet(cx + 20, top, damage=15, bullet_type='yellow_main')
            angle_left = math.radians(225)
            angle_right = math.radians(315)
            spd = 16
            Bullet(cx - 25, top, damage=10,
                   speed_x=spd * math.cos(angle_left), speed_y=spd * math.sin(angle_left),
                   bullet_type='yellow_small_left')
            Bullet(cx + 25, top, damage=10,
                   speed_x=spd * math.cos(angle_right), speed_y=spd * math.sin(angle_right),
                   bullet_type='yellow_small_right')
        elif lvl == 4:
            Bullet(cx - 20, top, damage=15, bullet_type='yellow_main')
            Bullet(cx - 7, top, damage=10, bullet_type='yellow_small')
            Bullet(cx + 7, top, damage=10, bullet_type='yellow_small')
            Bullet(cx + 20, top, damage=15, bullet_type='yellow_main')
            spd = 16
            angle_left1 = math.radians(200)
            angle_left2 = math.radians(250)
            angle_right1 = math.radians(290)
            angle_right2 = math.radians(340)
            Bullet(cx - 25, top - 5, damage=10,
                   speed_x=spd * math.cos(angle_left1), speed_y=spd * math.sin(angle_left1),
                   bullet_type='yellow_small_left')
            Bullet(cx - 25, top + 5, damage=10,
                   speed_x=spd * math.cos(angle_left2), speed_y=spd * math.sin(angle_left2),
                   bullet_type='yellow_small_left')
            Bullet(cx + 25, top - 5, damage=10,
                   speed_x=spd * math.cos(angle_right1), speed_y=spd * math.sin(angle_right1),
                   bullet_type='yellow_small_right')
            Bullet(cx + 25, top + 5, damage=10,
                   speed_x=spd * math.cos(angle_right2), speed_y=spd * math.sin(angle_right2),
                   bullet_type='yellow_small_right')
        elif lvl == 5:
            Bullet(cx - 20, top, damage=15, bullet_type='yellow_main')
            Bullet(cx - 7, top, damage=10, bullet_type='yellow_small')
            Bullet(cx + 7, top, damage=10, bullet_type='yellow_small')
            Bullet(cx + 20, top, damage=15, bullet_type='yellow_main')
            spd = 16
            left_angles = [200, 220, 240]
            for ang in left_angles:
                rad = math.radians(ang)
                Bullet(cx - 25, top, damage=10,
                       speed_x=spd * math.cos(rad),
                       speed_y=spd * math.sin(rad),
                       bullet_type='yellow_small_left')
            right_angles = [300, 320, 340]
            for ang in right_angles:
                rad = math.radians(ang)
                Bullet(cx + 25, top, damage=10,
                       speed_x=spd * math.cos(rad),
                       speed_y=spd * math.sin(rad),
                       bullet_type='yellow_small_right')

    def shoot_blue(self):
        lvl = self.weapon_level_blue
        cx, top = self.rect.centerx, self.rect.top
        if lvl == 1:
            Bullet(cx - 20, top, damage=10, bullet_type='yellow_main', penetrate=0)
            Bullet(cx - 7, top, damage=8, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 7, top, damage=8, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 20, top, damage=10, bullet_type='yellow_main', penetrate=0)
        elif lvl == 2:
            Bullet(cx - 20, top, damage=10, bullet_type='blue_large', penetrate=2)
            Bullet(cx - 7, top, damage=8, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 7, top, damage=8, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 20, top, damage=10, bullet_type='blue_large', penetrate=2)
        elif lvl == 3:
            offsets = [-20, -7, 7, 20]
            for off in offsets:
                Bullet(cx + off, top, damage=10, bullet_type='blue_large', penetrate=2)
        elif lvl == 4:
            Bullet(cx - 20, top, damage=10, bullet_type='blue_large', penetrate=2)
            Bullet(cx + 20, top, damage=10, bullet_type='blue_large', penetrate=2)
            now = pygame.time.get_ticks()
            if now - self.laser_shot_timer >= 150:
                self.laser_shot_timer = now
                LaserBeam(cx - 1, top, frames=laser_frames)
        elif lvl >= 5:
            Bullet(cx - 20, top, damage=10, bullet_type='blue_large', penetrate=2)
            Bullet(cx + 20, top, damage=10, bullet_type='blue_large', penetrate=2)
            now = pygame.time.get_ticks()
            if now - self.laser_shot_timer >= 150:
                self.laser_shot_timer = now
                LaserBeam(cx - 11, top, frames=laser_frames)
                LaserBeam(cx + 9, top, frames=laser_frames)

    def shoot_red(self):
        lvl = self.weapon_level_red
        cx, top = self.rect.centerx, self.rect.top
        red31_speed = RED_SPEED
        red32_speed = RED_SPEED
        red33_speed = RED_SPEED
        red34_speed = RED_SPEED
        if lvl == 1:
            Bullet(cx, top, damage=40, speed_y=red31_speed, bullet_type='red_31')
        elif lvl == 2:
            Bullet(cx - 15, top, damage=20, speed_y=red32_speed, bullet_type='red_32')
            Bullet(cx, top, damage=30, speed_y=red31_speed, bullet_type='red_31')
            Bullet(cx + 15, top, damage=20, speed_y=red32_speed, bullet_type='red_32')
        elif lvl == 3:
            Bullet(cx, top, damage=110, speed_y=red33_speed, bullet_type='red_33')
        elif lvl == 4:
            Bullet(cx, top, damage=110, speed_y=red33_speed, bullet_type='red_33')
            now = pygame.time.get_ticks()
            if now - self.missile_last_shoot >= self.missile_cooldown:
                m1 = HomingMissile(cx - 15, top)
                m2 = HomingMissile(cx + 15, top)
                all_sprites.add(m1, m2)
                bullets.add(m1, m2)
                self.missile_last_shoot = now
        elif lvl >= 5:
            Bullet(cx, top, damage=160, speed_y=red34_speed, bullet_type='red_34')
            now = pygame.time.get_ticks()
            if now - self.missile_last_shoot >= self.missile_cooldown:
                m1 = HomingMissile(cx - 15, top)
                m2 = HomingMissile(cx + 15, top)
                all_sprites.add(m1, m2)
                bullets.add(m1, m2)
                self.missile_last_shoot = now

    def activate_ult(self):
        if self.dying or self.ult_charges <= 0 or self.ultimate_active:
            return False
        if self.weapon_type == 'red':
            self.ult_charges -= 1
            self.ultimate_active = True
            w = Wormhole(self)
            all_sprites.add(w)
            return True
        elif self.weapon_type == 'blue' and self.weapon_level_blue >= 1:
            self.ult_charges -= 1
            self.ultimate_active = True
            self.ultimate_preparing = True
            self.ultimate_timer = pygame.time.get_ticks()
            self.ultimate_animation_frame = 0
            self.ultimate_last_update = pygame.time.get_ticks()
            return True
        else:
            self.ult_charges -= 1
            nuke = NukeBullet(self.rect.centerx, self.rect.top)
            all_sprites.add(nuke)
            return True

    def add_ult_charge(self):
        self.ult_charges += 1

    def apply_upgrade(self, powerup):
        if powerup.type == 'ultimate':
            self.add_ult_charge()
            return
        color = powerup.current_color if hasattr(powerup, 'current_color') else powerup.type
        if color == self.weapon_type:
            if color == 'yellow':
                if self.weapon_level_yellow < 5:
                    self.weapon_level_yellow += 1
                else:
                    self.activate_overload()
            elif color == 'blue':
                if self.weapon_level_blue < 5:
                    self.weapon_level_blue += 1
                else:
                    self.activate_overload()
            elif color == 'red':
                if self.weapon_level_red < 5:
                    self.weapon_level_red += 1
                else:
                    self.activate_overload()
        else:
            self.weapon_type = color
            if color == 'yellow':
                self.weapon_level_yellow = max(self.weapon_level_yellow, 1)
            elif color == 'blue':
                self.weapon_level_blue = max(self.weapon_level_blue, 1)
            elif color == 'red':
                self.weapon_level_red = max(self.weapon_level_red, 1)

    def activate_overload(self):
        cx, cy = self.rect.centerx, self.rect.top
        if self.weapon_type == 'yellow':
            for angle in range(0, 360, 30):
                rad = math.radians(angle)
                spd = 10
                YellowOverloadBullet(cx, cy, speed_x=spd * math.cos(rad), speed_y=spd * math.sin(rad))
        elif self.weapon_type == 'blue':
            for angle in range(0, 360, 30):
                rad = math.radians(angle)
                spd = 8
                BlueOverloadBullet(cx, cy, speed_x=spd * math.cos(rad), speed_y=spd * math.sin(rad))
        else:  # red
            for angle in range(0, 360, 30):
                rad = math.radians(angle)
                spd = 5
                RedOverloadBullet(cx, cy, speed_x=spd * math.cos(rad), speed_y=spd * math.sin(rad))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, damage=10, speed_x=0, speed_y=-25, bullet_type='yellow_main', penetrate=0):
        super().__init__()
        self.damage = damage
        self.penetrate = penetrate
        if penetrate == -1:
            self.hits_left = -1
        else:
            self.hits_left = penetrate + 1
        self.bullet_type = bullet_type
        if bullet_type == 'yellow_small':
            self.image = bullet_small_img.copy()
        elif bullet_type == 'yellow_small_left':
            self.image = bullet_small_left_img.copy()
        elif bullet_type == 'yellow_small_right':
            self.image = bullet_small_right_img.copy()
        elif bullet_type == 'yellow_main':
            self.image = pygame.transform.scale(bullet1_1_img, (12, 40))
        elif bullet_type == 'blue_small':
            self.image = bullet2_1_img.copy()
        elif bullet_type == 'blue_medium':
            self.image = bullet2_2_img.copy()
        elif bullet_type == 'blue_large':
            self.image = bullet2_2_img.copy()
        elif bullet_type == 'overload':
            self.image = overload_img.copy()
        elif bullet_type == 'red_31':
            self.image = bullet3_1_img.copy()
        elif bullet_type == 'red_32':
            self.image = bullet3_2_img.copy()
        elif bullet_type == 'red_33':
            self.image = bullet3_3_img.copy()
        elif bullet_type == 'red_34':
            self.image = bullet3_4_img.copy()
        else:
            self.image = pygame.Surface((10, 20))
            self.image.fill(WHITE)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = max(self.rect.width, self.rect.height) // 2  # 用于圆形碰撞
        self.already_hit = []
        all_sprites.add(self)
        bullets.add(self)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
            return
        if self.hits_left != -1 and self.hits_left <= 0:
            self.kill()
            return
        all_enemies = list(rocks) + list(enemy1_group) + list(enemy2_group) + list(enemy3_group) + \
                      list(enemy4_group) + list(enemy6_group) + list(enemy7_group) + list(enemy8_group) + \
                      list(enemy13_group) + list(boss_group) + list(special_enemies) + \
                      list(enemy5_group) + list(enemy9_group) + list(enemy10_group) + list(enemy11_group) + list(enemy12_group)
        for enemy in all_enemies:
            if enemy in self.already_hit:
                continue
            # 根据敌机类型选择碰撞形状
            if isinstance(enemy, Enemy5):
                enemy_rect = enemy.rect
                hit = self.rect.colliderect(enemy_rect)
            elif isinstance(enemy, (Enemy9, Enemy10, Enemy11, Enemy12)):
                dx = self.rect.centerx - enemy.rect.centerx
                dy = self.rect.centery - enemy.rect.centery
                dist = math.hypot(dx, dy)
                enemy_radius = getattr(enemy, 'radius', 20)
                hit = dist < enemy_radius + self.radius
                enemy_rect = enemy.rect  # 用于爆炸位置
            else:
                # 原有敌人保留原碰撞方式（矩形或hitbox_rect）
                enemy_rect = getattr(enemy, 'hitbox_rect', enemy.rect)
                hit = self.rect.colliderect(enemy_rect)
            if hit:
                enemy.take_damage(self.damage)
                hit_effect = HitExplosion(enemy.rect.centerx, enemy.rect.centery)
                all_sprites.add(hit_effect)
                self.already_hit.append(enemy)
                if self.hits_left != -1:
                    self.hits_left -= 1
                    if self.hits_left <= 0:
                        self.kill()
                break


class LaserBeam(pygame.sprite.Sprite):
    def __init__(self, x, player_top_y, frames):
        super().__init__()
        self.frames = frames
        self.frame_index = 0
        self.frame_duration = 100
        self.last_update = pygame.time.get_ticks()
        beam_width = 30
        beam_height = max(1, player_top_y)
        self.rect = pygame.Rect(0, 0, beam_width, beam_height)
        self.rect.centerx = x
        self.rect.bottom = player_top_y
        self.rect.top = 0
        self.scaled_frames = []
        for f in self.frames:
            scaled = pygame.transform.smoothscale(f, (beam_width, beam_height))
            self.scaled_frames.append(scaled)
        self.image = self.scaled_frames[0]
        self.damage = LASERBEAM_DAMAGE
        self.lifetime = 300
        self.born_time = pygame.time.get_ticks()
        self.damage_enemies()
        all_sprites.add(self)
        bullets.add(self)

    def damage_enemies(self):
        all_enemies = list(rocks) + list(enemy1_group) + list(enemy2_group) + list(enemy3_group) + \
                      list(enemy4_group) + list(enemy6_group) + list(enemy7_group) + list(enemy8_group) + \
                      list(enemy13_group) + list(boss_group) + list(special_enemies) + \
                      list(enemy5_group) + list(enemy9_group) + list(enemy10_group) + list(enemy11_group) + list(enemy12_group)
        for enemy in all_enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.damage)
                hit_effect = HitExplosion(enemy.rect.centerx, enemy.rect.centery)
                all_sprites.add(hit_effect)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.born_time > self.lifetime:
            self.kill()
            return
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.scaled_frames)
            self.image = self.scaled_frames[self.frame_index]


class SuperLaserBeam(pygame.sprite.Sprite):
    def __init__(self, x, player_top_y, beam_width, beam_height, frames, player):
        super().__init__()
        self.frames = frames
        self.frame_index = 0
        self.frame_duration = 100
        self.last_update = pygame.time.get_ticks()
        self.beam_width = beam_width
        self.player = player
        self.image = pygame.transform.smoothscale(self.frames[0], (beam_width, beam_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = player_top_y
        self.rect.top = 0
        self.damage = 500
        self.lifetime = 300
        self.born_time = pygame.time.get_ticks()
        self.damage_enemies()

    def damage_enemies(self):
        all_enemies = list(rocks) + list(enemy1_group) + list(enemy2_group) + list(enemy3_group) + \
                      list(enemy4_group) + list(enemy6_group) + list(enemy7_group) + list(enemy8_group) + \
                      list(enemy13_group) + list(boss_group) + list(special_enemies) + \
                      list(enemy5_group) + list(enemy9_group) + list(enemy10_group) + list(enemy11_group) + list(enemy12_group)
        for enemy in all_enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.damage)
                hit_effect = HitExplosion(enemy.rect.centerx, enemy.rect.centery)
                all_sprites.add(hit_effect)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.born_time > self.lifetime:
            self.kill()
            return
        new_bottom = self.player.rect.top
        if new_bottom < 0:
            new_bottom = 0
        new_height = max(1, new_bottom)
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = pygame.transform.smoothscale(
                self.frames[self.frame_index], (self.beam_width, new_height))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.player.rect.centerx
            self.rect.bottom = new_bottom
            self.rect.top = 0
        else:
            self.rect.centerx = self.player.rect.centerx
            self.rect.bottom = new_bottom
            self.rect.top = 0


class YellowOverloadBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()
        self.image = overload_img.copy()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.damage = 300
        self.already_hit = []
        all_sprites.add(self)
        bullets.add(self)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
            return
        all_enemies = list(rocks) + list(enemy1_group) + list(enemy2_group) + list(enemy3_group) + \
                      list(enemy4_group) + list(enemy6_group) + list(enemy7_group) + list(enemy8_group) + \
                      list(enemy13_group) + list(boss_group) + list(special_enemies) + \
                      list(enemy5_group) + list(enemy9_group) + list(enemy10_group) + list(enemy11_group) + list(enemy12_group)
        for enemy in all_enemies:
            if enemy in self.already_hit:
                continue
            enemy_rect = getattr(enemy, 'hitbox_rect', enemy.rect)
            if self.rect.colliderect(enemy_rect):
                enemy.take_damage(self.damage)
                hit_effect = HitExplosion(enemy.rect.centerx, enemy.rect.centery)
                all_sprites.add(hit_effect)
                self.already_hit.append(enemy)
                self.kill()
                return


class BlueOverloadBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()
        self.image = enemy_bullet_img3.copy()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.damage = 150
        self.already_hit = []
        all_sprites.add(self)
        bullets.add(self)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
            return
        all_enemies = list(rocks) + list(enemy1_group) + list(enemy2_group) + list(enemy3_group) + \
                      list(enemy4_group) + list(enemy6_group) + list(enemy7_group) + list(enemy8_group) + \
                      list(enemy13_group) + list(boss_group) + list(special_enemies) + \
                      list(enemy5_group) + list(enemy9_group) + list(enemy10_group) + list(enemy11_group) + list(enemy12_group)
        for enemy in all_enemies:
            if enemy in self.already_hit:
                continue
            enemy_rect = getattr(enemy, 'hitbox_rect', enemy.rect)
            if self.rect.colliderect(enemy_rect):
                enemy.take_damage(self.damage)
                hit_effect = HitExplosion(enemy.rect.centerx, enemy.rect.centery)
                all_sprites.add(hit_effect)
                self.already_hit.append(enemy)


class RedOverloadBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()
        self.original_image = overload2_img.copy()
        angle = math.degrees(math.atan2(speed_x, speed_y))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.damage = 200
        self.born_time = pygame.time.get_ticks()
        self.fly_duration = 500
        self.life_duration = 10000
        self.stopped = False
        all_sprites.add(self)
        bullets.add(self)

    def move_with_bg(self, offset_change):
        if self.stopped:
            self.rect.x += offset_change

    def update(self):
        now = pygame.time.get_ticks()
        elapsed = now - self.born_time
        if not self.stopped:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            if elapsed >= self.fly_duration:
                self.stopped = True
                self.speed_x = 0
                self.speed_y = 0
        else:
            all_enemies = list(rocks) + list(enemy1_group) + list(enemy2_group) + list(enemy3_group) + \
                          list(enemy4_group) + list(enemy6_group) + list(enemy7_group) + list(enemy8_group) + \
                          list(enemy13_group) + list(boss_group) + list(special_enemies) + \
                          list(enemy5_group) + list(enemy9_group) + list(enemy10_group) + list(enemy11_group) + list(enemy12_group)
            for enemy in all_enemies:
                if self.rect.colliderect(enemy.rect):
                    enemy.take_damage(self.damage)
                    hit_effect = HitExplosion(enemy.rect.centerx, enemy.rect.centery)
                    all_sprites.add(hit_effect)
                    self.kill()
                    return
        if elapsed >= self.fly_duration + self.life_duration:
            self.kill()
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()


class EnemyLaserBeam(pygame.sprite.Sprite):
    def __init__(self, x, top_y, parent_enemy):
        super().__init__()
        self.parent_enemy = parent_enemy
        # 记录相对于敌机中心的水平偏移
        self.offset_x = x - parent_enemy.rect.centerx

        self.orig_image = enemy_bullet_laser_img
        self.visual_width = 50          # 视觉宽度
        self.collision_width = 10       # 碰撞宽度（单独调节）

        height = HEIGHT - top_y
        # 碰撞矩形使用 collision_width，图像使用 visual_width
        self.rect = pygame.Rect(0, 0, self.collision_width, height)
        self.rect.centerx = x
        self.rect.top = top_y
        self.image = pygame.transform.scale(self.orig_image, (self.visual_width, height))

        self.damage = 100
        self.lifetime = 2000
        self.born_time = pygame.time.get_ticks()


    def move_with_bg(self, offset_change):
        # 激光跟随敌机，不受背景偏移影响
        pass

    def update(self):
        if self.parent_enemy is None or not self.parent_enemy.alive():
            self.kill()
            return
        if pygame.time.get_ticks() - self.born_time > self.lifetime:
            self.kill()
            return

        # 跟随敌机，保持水平偏移
        self.rect.centerx = self.parent_enemy.rect.centerx + self.offset_x
        self.rect.top = self.parent_enemy.rect.bottom
        self.rect.height = HEIGHT - self.rect.top
        if self.rect.height <= 0:
            self.kill()
            return

        # 图像按视觉宽度缩放
        self.image = pygame.transform.scale(self.orig_image,(self.visual_width, self.rect.height))


class BossLaserBeam(EnemyLaserBeam):
    def __init__(self, x, top_y, parent_enemy, emitter_y_offset=0):
        super().__init__(x, top_y, parent_enemy)
        self.emitter_y_offset = emitter_y_offset  # 从飞机顶部向上偏移（通常为0或正值表示更上方）

    def update(self):
        if self.parent_enemy is None or not self.parent_enemy.alive():
            self.kill()
            return
        if pygame.time.get_ticks() - self.born_time > self.lifetime:
            self.kill()
            return
        # 从飞机上方发射：顶部 = 敌机顶部 - 偏移量
        new_top = self.parent_enemy.rect.top - self.emitter_y_offset
        self.rect.top = new_top
        self.rect.height = HEIGHT - new_top
        if self.rect.height <= 0:
            self.kill()
            return
        self.rect.centerx = self.parent_enemy.rect.centerx + self.offset_x
        self.image = pygame.transform.scale(self.orig_image, (self.visual_width, self.rect.height))


class BossLaserBeamDown(pygame.sprite.Sprite):
    def __init__(self, x, top_y, parent_enemy):
        super().__init__()
        self.parent_enemy = parent_enemy
        # 保存相对于敌机中心的水平偏移
        self.offset_x = x - parent_enemy.rect.centerx
        # 保存相对于敌机底部的垂直偏移（top_y - 敌机底部）
        self.offset_y_from_bottom = top_y - parent_enemy.rect.bottom

        self.orig_image = enemy_bullet_laser_img
        self.visual_width = 50
        self.collision_width = 10

        height = HEIGHT - top_y
        self.rect = pygame.Rect(0, 0, self.collision_width, height)
        self.rect.centerx = x
        self.rect.top = top_y
        self.image = pygame.transform.scale(self.orig_image, (self.visual_width, height))

        self.damage = 100
        self.lifetime = 2000
        self.born_time = pygame.time.get_ticks()

    def update(self):
        if self.parent_enemy is None or not self.parent_enemy.alive():
            self.kill()
            return
        if pygame.time.get_ticks() - self.born_time > self.lifetime:
            self.kill()
            return

        # 跟随敌机水平位置
        self.rect.centerx = self.parent_enemy.rect.centerx + self.offset_x
        # 顶部 = 敌机底部 + 初始偏移量
        self.rect.top = self.parent_enemy.rect.bottom + self.offset_y_from_bottom
        self.rect.height = HEIGHT - self.rect.top
        if self.rect.height <= 0:
            self.kill()
            return
        self.image = pygame.transform.scale(self.orig_image, (self.visual_width, self.rect.height))

    def move_with_bg(self, offset_change):
        pass  # 激光跟随敌机，不受背景偏移影响


# ------------------------- 刷怪辅助函数 -------------------------
def spawn_enemy1(x_list):
    for x in x_list:
        e = Enemy1(x)
        all_sprites.add(e)
        enemy1_group.add(e)

def spawn_enemy2(x_list):
    for x in x_list:
        e = Enemy2(x)
        all_sprites.add(e)
        enemy2_group.add(e)

def spawn_enemy3(x_list):
    for x in x_list:
        e = Enemy3(x)
        all_sprites.add(e)
        enemy3_group.add(e)

def spawn_enemy4(x_list):
    for x in x_list:
        e = Enemy4(x)
        all_sprites.add(e)
        enemy4_group.add(e)

def spawn_enemy6(x_list):
    for x in x_list:
        e = Enemy6(x)
        all_sprites.add(e)
        enemy6_group.add(e)

def spawn_enemy7(x_list):
    for x in x_list:
        e = Enemy7(x)
        all_sprites.add(e)
        enemy7_group.add(e)

def spawn_enemy8(x_list):
    for x in x_list:
        e = Enemy8(x)
        all_sprites.add(e)
        enemy8_group.add(e)

def spawn_enemy13(x_list):
    for x in x_list:
        e = Enemy13(x)
        all_sprites.add(e)
        enemy13_group.add(e)

def spawn_enemy5(x_list):
    for x in x_list:
        e = Enemy5(x)
        all_sprites.add(e)
        enemy5_group.add(e)

def spawn_enemy9(x_list):
    for x in x_list:
        e = Enemy9(x)
        all_sprites.add(e)
        enemy9_group.add(e)

def spawn_enemy10(x_list):
    for x in x_list:
        e = Enemy10(x)
        all_sprites.add(e)
        enemy10_group.add(e)

def spawn_enemy11(x_list):
    for x in x_list:
        e = Enemy11(x)
        all_sprites.add(e)
        enemy11_group.add(e)

def spawn_enemy12(x_list):
    for x in x_list:
        e = Enemy12(x)
        all_sprites.add(e)
        enemy12_group.add(e)

def spawn_sp1(x, drop_color="yellow"):
    sp = EnemySp1(x, drop_color)
    all_sprites.add(sp)
    special_enemies.add(sp)

def spawn_sp2(x):
    sp = EnemySp2(x)
    all_sprites.add(sp)
    special_enemies.add(sp)

def spawn_boss1():
    boss = Boss1()
    all_sprites.add(boss)
    boss_group.add(boss)

def spawn_boss2():
    boss = Boss2()
    all_sprites.add(boss)
    boss_group.add(boss)

def spawn_boss3():
    boss = Boss3()
    all_sprites.add(boss)
    boss_group.add(boss)

def spawn_boss4():
    boss = Boss4()
    all_sprites.add(boss)
    boss_group.add(boss)

def spawn_rock(x):
    r = Rock(x)
    all_sprites.add(r)
    rocks.add(r)

def spawn_rocks(x_list):
    for x in x_list:
        spawn_rock(x)


def reset_game(level, keep_weapon=False):
    global game_over, game_over_start
    game_over = False
    game_over_start = 0
    global all_sprites, rocks, enemy1_group, enemy2_group, enemy3_group, enemy4_group, enemy6_group, enemy7_group, enemy8_group, boss_group, bullets
    global enemy_bullets, powerups, special_enemies, enemy13_group, enemy5_group, enemy9_group, enemy10_group, enemy11_group, enemy12_group
    global player, bg_offset, last_bg_offset, game_stage, stage_start_time
    global boss_spawned, triggered_events, background_img, bg1_y, bg2_y, space_was_pressed

    saved_weapon = None
    if keep_weapon and player is not None:
        saved_weapon = {
            'type': player.weapon_type,
            'yellow': player.weapon_level_yellow,
            'blue': player.weapon_level_blue,
            'red': player.weapon_level_red,
        }

    all_sprites.empty()
    rocks.empty()
    enemy1_group.empty()
    enemy2_group.empty()
    enemy3_group.empty()
    enemy4_group.empty()
    enemy6_group.empty()
    enemy7_group.empty()
    enemy8_group.empty()
    enemy13_group.empty()
    enemy5_group.empty()
    enemy9_group.empty()
    enemy10_group.empty()
    enemy11_group.empty()
    enemy12_group.empty()
    boss_group.empty()
    bullets.empty()
    enemy_bullets.empty()
    powerups.empty()
    special_enemies.empty()
    player = Player()
    all_sprites.add(player)

    if saved_weapon is not None:
        player.weapon_type = saved_weapon['type']
        player.weapon_level_yellow = saved_weapon['yellow']
        player.weapon_level_blue = saved_weapon['blue']
        player.weapon_level_red = saved_weapon['red']

    if level == 1:
        background_img = background_img1
    elif level == 2:
        background_img = background_img2
    elif level == 3:
        background_img = background_img3
    elif level == 4:
        background_img = background_img4
    bg1_y = 0
    bg2_y = -HEIGHT
    bg_offset = (player.rect.centerx - WIDTH / 2) * -0.12
    last_bg_offset = bg_offset
    game_stage = STAGE_1
    stage_start_time = pygame.time.get_ticks()
    game_over = False
    boss_spawned = False
    space_was_pressed = False
    triggered_events = {stage: [] for stage in STAGE_DURATION.keys()}


# ------------------------- 菜单函数 -------------------------
def draw_main_menu():
    screen.blit(menu_bg_double, (menu_bg_x, 0))
    # 整体下移量：标题起始 Y 坐标从 100 改为 160
    title = title_font.render("Stellar Secret Operations", True, WHITE)
    title_rect = title.get_rect(centerx=WIDTH // 2, y=160)
    screen.blit(title, title_rect)

    # 副标题：星秘行动
    subtitle = menu_font.render("星秘行动", True, WHITE)
    subtitle_rect = subtitle.get_rect(centerx=WIDTH // 2, y=title_rect.bottom + 10)
    screen.blit(subtitle, subtitle_rect)

    btn_width = 250
    btn_height = 60
    center_x = WIDTH // 2
    start_y = subtitle_rect.bottom + 60   # 按钮在副标题下方留出足够空间
    spacing = 80

    single_rect = pygame.Rect(center_x - btn_width // 2, start_y, btn_width, btn_height)
    multi_rect = pygame.Rect(center_x - btn_width // 2, start_y + spacing, btn_width, btn_height)
    exit_rect = pygame.Rect(center_x - btn_width // 2, start_y + spacing * 2, btn_width, btn_height)

    mouse = pygame.mouse.get_pos()

    color = YELLOW if single_rect.collidepoint(mouse) else WHITE
    pygame.draw.rect(screen, color, single_rect, 2)
    txt = menu_font.render("1 Player Game", True, color)
    screen.blit(txt, (single_rect.centerx - txt.get_width() // 2, single_rect.centery - txt.get_height() // 2))

    pygame.draw.rect(screen, GRAY, multi_rect, 2)
    txt = menu_font.render("2 Players Game", True, GRAY)
    screen.blit(txt, (multi_rect.centerx - txt.get_width() // 2, multi_rect.centery - txt.get_height() // 2))

    color = YELLOW if exit_rect.collidepoint(mouse) else WHITE
    pygame.draw.rect(screen, color, exit_rect, 2)
    txt = menu_font.render("Exit", True, color)
    screen.blit(txt, (exit_rect.centerx - txt.get_width() // 2, exit_rect.centery - txt.get_height() // 2))

    for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
        if event.button == 1:
            if single_rect.collidepoint(event.pos):
                return STATE_LEVEL_SELECT
            if exit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    return STATE_MENU

def draw_level_select():
    screen.blit(menu_bg_double, (menu_bg_x, 0))
    title = title_font.render("Select Level", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    btn_width = 250
    btn_height = 60
    center_x = WIDTH // 2
    start_y = 300
    spacing = 80

    levels = [1, 2, 3, 4]
    rects = {}
    mouse = pygame.mouse.get_pos()

    for i, lvl in enumerate(levels):
        rect = pygame.Rect(center_x - btn_width // 2, start_y + i * spacing, btn_width, btn_height)
        rects[lvl] = rect
        unlocked = lvl <= unlocked_levels
        if unlocked:
            color = YELLOW if rect.collidepoint(mouse) else WHITE
        else:
            color = GRAY
        pygame.draw.rect(screen, color, rect, 2)
        text = menu_font.render(f"Level {lvl}", True, color)
        screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

    back_rect = pygame.Rect(center_x - btn_width // 2, start_y + len(levels) * spacing, btn_width, btn_height)
    color = YELLOW if back_rect.collidepoint(mouse) else WHITE
    pygame.draw.rect(screen, color, back_rect, 2)
    txt = menu_font.render("Back", True, color)
    screen.blit(txt, (back_rect.centerx - txt.get_width() // 2, back_rect.centery - txt.get_height() // 2))

    for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
        if event.button == 1:
            for lvl, rect in rects.items():
                if rect.collidepoint(event.pos) and lvl <= unlocked_levels:
                    global current_level, game_state
                    current_level = lvl
                    reset_game(lvl)
                    game_state = STATE_PLAYING
                    return STATE_PLAYING
            if back_rect.collidepoint(event.pos):
                return STATE_MENU

    return STATE_LEVEL_SELECT


final_win_text = (
    "致顺利攻克所有关卡的每一位飞行员：\n"
    "当最后一架敌方战机陨落，\n"
    "《Stellar Secret Operations（星秘行动）》\n"
    "的全主线旅程就此落幕。\n"
    "这款飞行射击作品，是我以 Python 编程语言独立完成的项目，\n"
    "开发参考了哔哩哔哩UP主【易小时课堂】3小时Python打飞机小游戏制作教程，\n"
    "从代码搭建、敌机逻辑到关卡排布，全程耗时一个月打磨落地。\n"
    "创作的初心，源自陪伴我童年的第一款空战游戏 ——《恶魔之星》，\n"
    "是旧日的游戏回忆，催生了我亲手打造专属星空空战的想法。\n"
    "非常感谢你愿意花费时间，踏入这片星际战场,\n"
    "通关全部关卡便是对这份小众创作最大的认可。\n"
    "星海征途暂告一段落，但游戏带来的热血与快乐永不落幕。\n"
    "若未来新作问世，期待再次与你并肩翱翔于星际之上。\n"
)

final_win_text_index = 0
final_win_last_update = 0

# 主循环
running = True
while running:
    if game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.blit(background_img, (bg_offset - MAX_BG_OFFSET, bg1_y))
        screen.blit(background_img, (bg_offset - MAX_BG_OFFSET, bg2_y))
        all_sprites.draw(screen)
        go_text = title_font.render("GAME OVER", True, WHITE)
        screen.blit(go_text, (WIDTH // 2 - go_text.get_width() // 2, (HEIGHT // 2) - 80))
        pygame.display.flip()
        if pygame.time.get_ticks() - game_over_start >= 3000:
            game_over = False
            game_state = STATE_LEVEL_SELECT
        continue

    clock.tick(FPS)

    for event in pygame.event.get(pygame.QUIT):
        if event.type == pygame.QUIT:
            running = False

    menu_bg_x += menu_bg_speed
    if menu_bg_x <= -WIDTH:
        menu_bg_x = 0

    now_time = pygame.time.get_ticks()

    if game_state == STATE_MENU:
        game_state = draw_main_menu()
        pygame.display.flip()
        continue

    if game_state == STATE_LEVEL_SELECT:
        game_state = draw_level_select()
        pygame.display.flip()
        continue

    # ========== 最终通关状态（正确位置） ==========
    if game_state == STATE_FINAL_WIN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = STATE_MENU
                    # 重置文本索引，以便下次通关时重新显示
                    final_win_text_index = 0
                    final_win_last_update = 0
                    continue

        # 允许玩家移动（但不射击）
        keys = pygame.key.get_pressed()
        if not player.dying:
            player.update()

        # 更新所有精灵（玩家、爆炸效果等）
        all_sprites.update()

        # 背景滚动
        bg1_y += bg_speed
        bg2_y += bg_speed
        if bg1_y >= HEIGHT: bg1_y = -HEIGHT
        if bg2_y >= HEIGHT: bg2_y = -HEIGHT

        # 背景偏移（保持视觉跟随玩家）
        bg_offset = (player.rect.centerx - WIDTH / 2) * -0.12 if not player.dying else bg_offset

        # 绘制背景和精灵
        screen.fill(BLACK)
        screen.blit(background_img, (bg_offset - MAX_BG_OFFSET, bg1_y))
        screen.blit(background_img, (bg_offset - MAX_BG_OFFSET, bg2_y))
        all_sprites.draw(screen)

        # 打字效果：每 50 毫秒增加一个字符
        now = pygame.time.get_ticks()
        if final_win_text_index < len(final_win_text) and now - final_win_last_update > 50:
            final_win_text_index += 1
            final_win_last_update = now

        # 分行显示已出现的文字
        lines = final_win_text.split('\n')
        y_offset = 150
        char_count = 0
        for line in lines:
            if char_count >= final_win_text_index:
                break
            end_idx = min(len(line), final_win_text_index - char_count)
            text_to_show = line[:end_idx]
            text_surf = font.render(text_to_show, True, WHITE)
            screen.blit(text_surf, (WIDTH // 2 - text_surf.get_width() // 2, y_offset))
            y_offset += text_surf.get_height() + 5
            char_count += len(line) + 1   # +1 补偿被 split 删除的 '\n'

        # 全部显示完后提示按 Enter
        if final_win_text_index >= len(final_win_text):
            prompt = font.render("按下 Enter 返回菜单", True, YELLOW)
            screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, y_offset + 20))

        pygame.display.flip()
        continue   # 跳过后续游戏进行中的逻辑

    # ========== 游戏进行中 ==========
    keys = pygame.key.get_pressed()
    # ========== 调试快捷键：直接跳到 Boss 战 ==========！！！！！！！！！！！！！
    if keys[pygame.K_F1]:  # 你可以换成 pygame.K_b 或其他键
        # 清除所有敌人和子弹
        for group in [rocks, enemy1_group, enemy2_group, enemy3_group, enemy4_group,
                      enemy6_group, enemy7_group, enemy8_group, enemy13_group,
                      enemy5_group, enemy9_group, enemy10_group, enemy11_group, enemy12_group,
                      special_enemies, boss_group]:
            for enemy in group:
                enemy.kill()
        for bullet in enemy_bullets:
            bullet.kill()

        # 设置 Boss 阶段
        game_stage = STAGE_BOSS
        stage_start_time = pygame.time.get_ticks()
        boss_spawned = False  # 确保下面会生成
        triggered_events[STAGE_BOSS] = []  # 清空可能的事件

        # 立即生成 Boss2（针对第2关调试）
        # 如果你想通用，可以判断 current_level
        if current_level == 2:
            spawn_boss2()
            boss_spawned = True
        # ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    space_pressed = keys[pygame.K_SPACE]
    if space_pressed and not space_was_pressed and not player.dying:
        player.activate_ult()
    space_was_pressed = space_pressed

    stage_elapsed = now_time - stage_start_time

    if game_stage in level_stage_events[current_level]:
        events = level_stage_events[current_level][game_stage]
        for idx, (time_ms, callback) in enumerate(events):
            if idx not in triggered_events[game_stage] and stage_elapsed >= time_ms:
                callback()
                triggered_events[game_stage].append(idx)

    if current_level == 4 and game_stage == STAGE_1 and stage_elapsed >= 5000:
        game_stage = STAGE_BOSS
        stage_start_time = now_time
        boss_spawned = False
        triggered_events[STAGE_BOSS] = []

    if game_stage == STAGE_BOSS and not boss_spawned:
        if current_level == 1:
            spawn_boss1()
        elif current_level == 2:
            spawn_boss2()
        elif current_level == 3:
            spawn_boss3()
        elif current_level == 4:
            spawn_boss4()
        boss_spawned = True

    if game_stage != STAGE_WIN:
        duration = STAGE_DURATION.get(game_stage, 0)
        if duration > 0 and stage_elapsed >= duration:
            if game_stage < STAGE_BOSS:
                game_stage += 1
                stage_start_time = now_time
                triggered_events[game_stage] = []

    if game_stage != STAGE_WIN:
        if not player.dying and not player.invincible:
            for bullet in list(enemy_bullets):
                if not bullet.alive():
                    continue
                if isinstance(bullet, EnemyLaserBeam):
                    # 激光：矩形碰撞，碰边就死
                    if pygame.sprite.collide_rect(player, bullet):
                        player.take_damage(0, direct_kill=True)
                else:
                    # 普通子弹：圆形碰撞
                    if pygame.sprite.collide_circle(player, bullet):
                        player.take_damage(bullet.damage, direct_kill=False)
                        hit_effect = HitExplosion(player.rect.centerx, player.rect.centery)
                        all_sprites.add(hit_effect)
                        if isinstance(bullet, EnemyBullet2):
                            small_expl = ExplosionEffect(player.rect.centerx, player.rect.centery,
                                                         small_player_explosion_frames)
                            all_sprites.add(small_expl)
                        bullet.kill()

        # 玩家与敌机碰撞（enemy5用矩形，其他用圆形）
        if not player.dying and not player.invincible:
            if pygame.sprite.spritecollide(player, enemy5_group, False, pygame.sprite.collide_rect):
                player.take_damage(0, direct_kill=True)
            for group in [rocks, enemy1_group, enemy2_group, enemy3_group,
                          enemy6_group, enemy7_group, enemy8_group, enemy13_group,
                          special_enemies, boss_group,
                          enemy9_group, enemy10_group, enemy11_group, enemy12_group]:
                if pygame.sprite.spritecollide(player, group, False, pygame.sprite.collide_circle):
                    player.take_damage(0, direct_kill=True)
                    break
            for e4 in enemy4_group:
                if player.rect.colliderect(e4.hitbox_rect):
                    player.take_damage(0, direct_kill=True)
                    break

    if not player.dying:
        eaten = pygame.sprite.spritecollide(player, powerups, True)
        for p in eaten:
            player.apply_upgrade(p)

    if (keys[pygame.K_LCTRL] and not player.dying and not player.ultimate_active
            and now_time - last_shoot > shoot_cooldown):
        player.shoot()
        last_shoot = now_time

    all_sprites.update()

    if player.dying:
        if not any(isinstance(s, PlayerExplosion) for s in all_sprites):
            if not player.respawn():
                game_state = STATE_LEVEL_SELECT
                continue

    screen.fill(BLACK)
    bg_offset = (player.rect.centerx - WIDTH / 2) * -0.12 if not player.dying else bg_offset
    offset_change = bg_offset - last_bg_offset
    for bullet in bullets:
        if isinstance(bullet, RedOverloadBullet):
            bullet.move_with_bg(offset_change)
    for rock in rocks: rock.move_with_bg(offset_change)
    for e1 in enemy1_group: e1.move_with_bg(offset_change)
    for e2 in enemy2_group: e2.move_with_bg(offset_change)
    for e3 in enemy3_group: e3.move_with_bg(offset_change)
    for e4 in enemy4_group: e4.move_with_bg(offset_change)
    for e6 in enemy6_group: e6.move_with_bg(offset_change)
    for e7 in enemy7_group: e7.move_with_bg(offset_change)
    for e8 in enemy8_group: e8.move_with_bg(offset_change)
    for e13 in enemy13_group: e13.move_with_bg(offset_change)
    for e5 in enemy5_group: e5.move_with_bg(offset_change)
    for e9 in enemy9_group: e9.move_with_bg(offset_change)
    for e10 in enemy10_group: e10.move_with_bg(offset_change)
    for e11 in enemy11_group: e11.move_with_bg(offset_change)
    for e12 in enemy12_group: e12.move_with_bg(offset_change)
    for eb in enemy_bullets: eb.move_with_bg(offset_change)
    for sp in special_enemies: sp.move_with_bg(offset_change)
    for pw in powerups: pw.move_with_bg(offset_change)

    last_bg_offset = bg_offset

    bg1_y += bg_speed
    bg2_y += bg_speed
    if bg1_y >= HEIGHT: bg1_y = -HEIGHT
    if bg2_y >= HEIGHT: bg2_y = -HEIGHT

    screen.blit(background_img, (bg_offset - MAX_BG_OFFSET, bg1_y))
    screen.blit(background_img, (bg_offset - MAX_BG_OFFSET, bg2_y))
    all_sprites.draw(screen)

    screen.blit(background_img, (bg_offset - MAX_BG_OFFSET, bg2_y))
    all_sprites.draw(screen)

    # ... 背景绘制和精灵绘制 ...
    all_sprites.draw(screen)

    # 任务开始提示（前5秒）
    if game_stage == STAGE_1 and stage_elapsed <= 5000:
        screen.blit(mission_start_img, mission_start_pos)

    # 胜利提示（非第四关）
    if game_stage == STAGE_WIN and current_level != 4:
        screen.blit(player_yes_img, player_yes_pos)

    # HUD ...

    # HUD
    icon_spacing = 5
    start_x = 10
    start_y = HEIGHT - 90
    up_text = font.render("1 UP", True, RED)  # 使用已有的 font 对象，红色
    up_text_x = start_x  # 与生命图标左对齐
    up_text_y = start_y - up_text.get_height() - 5  # 放在图标上方，留5像素间距
    screen.blit(up_text, (up_text_x, up_text_y))
    for i in range(player.lives):
        screen.blit(life_icon_img, (start_x + i * (LIFE_ICON_SIZE + icon_spacing), start_y))

    two_up_text = font.render("2 UP", True, BLUE)
    two_up_x = WIDTH - 10 - two_up_text.get_width()
    two_up_y = up_text_y  # 高度与 1 UP 相同
    screen.blit(two_up_text, (two_up_x, two_up_y))

    # 右侧 2 UP 下方：Press Start（白色）
    press_start_text = font.render("Press Start", True, WHITE)
    press_start_x = WIDTH - 10 - press_start_text.get_width()
    press_start_y = two_up_y + two_up_text.get_height() + 5
    screen.blit(press_start_text, (press_start_x, press_start_y))

    hp_label = font.render("HP:", True, WHITE)
    screen.blit(hp_label, (10, HEIGHT - 65))
    hp_icon_count = player.hp // 10
    if hp_icon_count > 10:
        hp_icon_count = 10
    label_width = hp_label.get_width()
    icon_start_x = 10 + label_width + 5
    hp_spacing = -2
    for i in range(hp_icon_count):
        screen.blit(hp_icon_img, (icon_start_x + i * (HP_ICON_WIDTH + hp_spacing), HEIGHT - 63))

    max_ult_icons = 15
    ult_icon_count = player.ult_charges
    if ult_icon_count > max_ult_icons:
        ult_icon_count = max_ult_icons
    ult_start_x = 10
    ult_start_y = HEIGHT - 30
    ult_spacing = 3
    for i in range(ult_icon_count):
        screen.blit(ultimate_icon_img, (ult_start_x + i * (ULT_ICON_SIZE + ult_spacing), ult_start_y))
    # 屏幕底部居中显示关卡
    level_text = font.render(f"LEVEL {current_level}", True, WHITE)
    level_text_x = WIDTH // 2 - level_text.get_width() // 2
    level_text_y = HEIGHT - 40
    screen.blit(level_text, (level_text_x, level_text_y))

    if game_stage == STAGE_WIN:
        win_text = font.render("MISSION COMPLETE", True, WHITE)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
        if pygame.time.get_ticks() - stage_start_time >= STAGE_DURATION[STAGE_WIN]:
            if current_level < 4:
                unlocked_levels = max(unlocked_levels, current_level + 1)
                current_level += 1
                reset_game(current_level, keep_weapon=True)
            else:
                game_state = STATE_MENU

    pygame.display.flip()

