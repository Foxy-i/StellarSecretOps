import pygame
import os
import math

FPS = 60
WIDTH, HEIGHT = 700, 900
MAX_BG_OFFSET = 40

# 敌人血量
ROCK_HP = 300
ENEMY1_HP = 200
ENEMY2_HP = 150
ENEMY4_HP = 800
BOSS1_HP = 10000
SP1_HP = 300
SP2_HP = 400

# 玩家属性
PLAYER_MAX_HP = 100
PLAYER_LIVES = 3
INVINCIBLE_DURATION = 2000
PLAYER_ULT_CHARGES = 3

# 颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

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
    STAGE_4: 20000,
    STAGE_BOSS: 0,
    STAGE_WIN: 10000,
}

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Stellar Secret Operations (星秘行动)')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# 图片加载
player1_img = pygame.image.load(os.path.join('gameImages', 'player1.png')).convert()
rock1_img = pygame.image.load(os.path.join('gameImages', 'rock1.png')).convert()
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

laser_frames = []
for i in range(1, 4):
    img = pygame.image.load(os.path.join('gameImages', f'bullet2.3_{i}.png')).convert_alpha()
    img = pygame.transform.scale(img, (12, 40))
    laser_frames.append(img)

enemy1_img = pygame.image.load(os.path.join('gameImages', 'enemy1.png')).convert()
enemy2_img = pygame.image.load(os.path.join('gameImages', 'enemy2.png')).convert()
boss_img = pygame.image.load(os.path.join('gameImages', 'boss1.png')).convert()
enemy_bullet_img = pygame.image.load(os.path.join('gameImages', 'EnemyBullet1.png')).convert()
enemysp1_img = pygame.image.load(os.path.join('gameImages', 'enemysp1.png')).convert()
enemysp2_img = pygame.image.load(os.path.join('gameImages', 'enemysp2.png')).convert()
enemy4_img = pygame.image.load(os.path.join('gameImages', 'enemy4.png')).convert()

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
overload2_img = pygame.image.load(os.path.join('gameImages', 'bullet2.2.png')).convert_alpha()
overload2_img = pygame.transform.scale(overload2_img, (8, 32))

life_icon_img = pygame.image.load(os.path.join('gameImages', 'life_icon.png')).convert_alpha()
LIFE_ICON_SIZE = 15
life_icon_img = pygame.transform.scale(life_icon_img, (LIFE_ICON_SIZE, LIFE_ICON_SIZE))

hp_icon_img = pygame.image.load(os.path.join('gameImages', 'hp_icon.png')).convert_alpha()
HP_ICON_WIDTH = 12
HP_ICON_HEIGHT = 24
hp_icon_img = pygame.transform.scale(hp_icon_img, (HP_ICON_WIDTH, HP_ICON_HEIGHT))

explosion_frames = []
for i in range(1, 13):
    filename = f'explosion_{i:02d}.png'
    path = os.path.join('gameImages', filename)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (400, 400))
    explosion_frames.append(img)

NukeBullet_img = pygame.image.load(os.path.join('gameImages', 'NukeBullet.png')).convert()

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

bg1_y = 0
bg2_y = -HEIGHT
bg_speed = 0.5

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
enemy1_group = pygame.sprite.Group()
enemy2_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
special_enemies = pygame.sprite.Group()
enemy4_group = pygame.sprite.Group()

game_stage = STAGE_1
stage_start_time = pygame.time.get_ticks()
game_over = False
shoot_cooldown = 120
last_shoot = 0
space_was_pressed = False

player_explosion_frames = []
for i in range(1, 11):
    filename = f'player_explode{i}.png'
    path = os.path.join('gameImages', filename)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (120, 120))
    player_explosion_frames.append(img)

# 玩家大招动画帧
player_laser_frames = []
for i in range(1, 7):
    img = pygame.image.load(os.path.join('gameImages', f'player_laser{i}.png')).convert_alpha()
    img = pygame.transform.scale(img, (50, 64))
    player_laser_frames.append(img)


class EnemyBase(pygame.sprite.Sprite):
    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.max_hp = hp

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
        self.speedy = 2
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


class EnemySp1(EnemyBase):
    def __init__(self, spawn_x):
        super().__init__(SP1_HP)
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
        drop = PowerUp(self.rect.centerx, self.rect.centery, 'yellow', color_cycle=True)
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
        hit_w = self.rect.width - 60
        hit_h = self.rect.height - 40
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
                eb = EnemyBullet(self.rect.centerx, self.rect.bottom)
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


class Boss1(EnemyBase):
    def __init__(self):
        super().__init__(BOSS1_HP)
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

    def burst_shoot_mode1(self):
        bullet_width = 16
        start_x = self.rect.left + bullet_width // 2
        end_x = self.rect.right - bullet_width // 2
        if end_x - start_x < bullet_width * 9:
            start_x = self.rect.centerx - bullet_width * 5
            end_x = self.rect.centerx + bullet_width * 5
        step = (end_x - start_x) / 9
        y_offsets = [self.rect.bottom + 5, self.rect.bottom + 21]
        for y_off in y_offsets:
            for i in range(10):
                x_pos = start_x + i * step
                eb = EnemyBullet(x_pos, y_off)
                eb.speedy = 7
                eb.speed_x = 0
                all_sprites.add(eb)
                enemy_bullets.add(eb)

    def burst_shoot_mode2(self):
        bullet_width = 16
        rows = 10
        cols = 5
        start_y = self.rect.bottom + 5
        end_y = self.rect.bottom + 5 + (rows - 1) * 15
        start_x = self.rect.left + bullet_width // 2
        end_x = self.rect.right - bullet_width // 2
        step_x = (end_x - start_x) / (cols - 1) if cols > 1 else 0
        for row in range(rows):
            y = start_y + row * 15
            for col in range(cols):
                x = start_x + col * step_x
                eb = EnemyBullet(x, y)
                eb.speedy = 7
                eb.speed_x = 0
                all_sprites.add(eb)
                enemy_bullets.add(eb)

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

    def update(self):
        if self.entering:
            self.rect.y += self.enter_speed
            if self.rect.y >= self.enter_target_y:
                self.rect.y = self.enter_target_y
                self.entering = False
                self.next_attack = pygame.time.get_ticks() + self.attack_interval
                self.rect.clamp_ip(self.move_area)
            return
        self.rect.x += self.speed_x
        if self.rect.left < self.move_area.left or self.rect.right > self.move_area.right:
            self.speed_x *= -1
            self.rect.clamp_ip(self.move_area)
        self.rect.y += self.speed_y
        if self.rect.top < self.move_area.top or self.rect.bottom > self.move_area.bottom:
            self.speed_y *= -1
            self.rect.clamp_ip(self.move_area)
        now = pygame.time.get_ticks()
        if now >= self.next_attack:
            if self.mode == 1:
                self.burst_shoot_mode1()
                self.mode = 2
            elif self.mode == 2:
                self.burst_shoot_mode2()
                self.mode = 3
            else:
                self.burst_shoot_mode3()
                self.mode = 1
            self.next_attack = now + self.attack_interval

    def move_with_bg(self, offset_change):
        pass


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, type='yellow', color_cycle=False):
        super().__init__()
        self.type = type
        self.color_cycle = color_cycle
        self.current_color = 'yellow'
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
            self.orig_image = self.color_images['yellow']
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
        if self.color_cycle and self.type != 'ultimate':
            now = pygame.time.get_ticks()
            elapsed = now - self.create_time
            cycle = (elapsed // 10000) % 3
            if cycle == 0:
                new_color = 'yellow'
            elif cycle == 1:
                new_color = 'blue'
            else:
                new_color = 'red'
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


class NukeBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(NukeBullet_img, (12, 35))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(x, y))
        self.speedy = -10
        self.damage = 1000
        self.explosion_radius = 300

    def update(self):
        self.rect.y += self.speedy
        hit_enemy = pygame.sprite.spritecollideany(self, rocks) or \
                    pygame.sprite.spritecollideany(self, enemy1_group) or \
                    pygame.sprite.spritecollideany(self, enemy2_group) or \
                    pygame.sprite.spritecollideany(self, boss_group) or \
                    pygame.sprite.spritecollideany(self, special_enemies) or \
                    pygame.sprite.spritecollideany(self, enemy4_group)
        if self.rect.centery <= HEIGHT // 3 or hit_enemy:
            self.explode()
            self.kill()

    def explode(self):
        for bullet in list(enemy_bullets):
            if math.hypot(bullet.rect.centerx - self.rect.centerx,
                          bullet.rect.centery - self.rect.centery) < self.explosion_radius:
                bullet.kill()
        all_enemies = (rocks.sprites() + enemy1_group.sprites() + enemy2_group.sprites() +
                       boss_group.sprites() + special_enemies.sprites() + enemy4_group.sprites())
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

        self.max_hp = PLAYER_MAX_HP
        self.hp = self.max_hp
        self.lives = PLAYER_LIVES
        self.invincible = False
        self.invincible_end_time = 0
        self.dying = False
        self.ult_charges = PLAYER_ULT_CHARGES

        self.laser_shot_timer = 0

        # 蓝色大招状态
        self.ultimate_active = False
        self.ultimate_preparing = False
        self.ultimate_beam_active = False
        self.ultimate_timer = 0
        self.ultimate_animation_frame = 0
        self.ultimate_last_update = 0
        self.ultimate_beam = None

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
            else:
                self.weapon_level_blue = max(0, self.weapon_level_blue - 2)
                if self.weapon_level_blue == 0:
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
            global game_over
            game_over = True
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

        now = pygame.time.get_ticks()

        # 大招状态处理
        if self.ultimate_active:
            if self.ultimate_preparing:
                elapsed = now - self.ultimate_timer
                if elapsed >= 2000:
                    self.ultimate_preparing = False
                    self.ultimate_beam_active = True
                    self.ultimate_timer = now
                    self.image = self.image_ori.copy()   # 蓄力结束，飞机恢复原样
                    beam_width = 150
                    beam_height = max(1, self.rect.top)
                    super_laser = SuperLaserBeam(self.rect.centerx, self.rect.top, beam_width, beam_height,
                                                 laser_frames)
                    all_sprites.add(super_laser)
                    bullets.add(super_laser)
                    self.ultimate_beam = super_laser
                else:
                    if now - self.ultimate_last_update > 100:
                        self.ultimate_last_update = now
                        self.ultimate_animation_frame = (self.ultimate_animation_frame + 1) % len(player_laser_frames)
                        self.image = player_laser_frames[self.ultimate_animation_frame]
            elif self.ultimate_beam_active:
                if self.ultimate_beam is None or not self.ultimate_beam.alive():
                    self.ultimate_active = False
                    self.ultimate_beam_active = False
                    self.image = self.image_ori.copy()
                else:
                    if self.ultimate_beam and self.ultimate_beam.alive():
                        self.ultimate_beam.rect.centerx = self.rect.centerx
                        new_bottom = self.rect.top
                        if new_bottom < 0:
                            new_bottom = 0
                        new_height = max(1, new_bottom)
                        if self.ultimate_beam.rect.height != new_height:
                            self.ultimate_beam.rect.height = new_height
                            self.ultimate_beam.rect.bottom = new_bottom
                            new_frames = []
                            for f in self.ultimate_beam.frames:
                                scaled = pygame.transform.scale(f, (self.ultimate_beam.rect.width, new_height))
                                new_frames.append(scaled)
                            self.ultimate_beam.scaled_frames = new_frames
                            self.ultimate_beam.image = self.ultimate_beam.scaled_frames[self.ultimate_beam.frame_index]
                        else:
                            self.ultimate_beam.rect.bottom = new_bottom
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
        if self.weapon_type == 'yellow':
            self.shoot_yellow()
        else:
            self.shoot_blue()

    def shoot_yellow(self):
        lvl = self.weapon_level_yellow
        cx, top = self.rect.centerx, self.rect.top
        if lvl == 0:
            Bullet(cx, top, damage=10, bullet_type='yellow_main')
        elif lvl == 1:
            Bullet(cx - 15, top, damage=9, bullet_type='yellow_main')
            Bullet(cx + 15, top, damage=9, bullet_type='yellow_main')
        elif lvl == 2:
            Bullet(cx - 20, top, damage=8, bullet_type='yellow_main')
            Bullet(cx - 8, top, damage=5, bullet_type='yellow_small')
            Bullet(cx + 5, top, damage=5, bullet_type='yellow_small')
            Bullet(cx + 20, top, damage=8, bullet_type='yellow_main')
        elif lvl == 3:
            Bullet(cx - 20, top, damage=8, bullet_type='yellow_main')
            Bullet(cx - 8, top, damage=5, bullet_type='yellow_small')
            Bullet(cx + 5, top, damage=5, bullet_type='yellow_small')
            Bullet(cx + 20, top, damage=8, bullet_type='yellow_main')
            angle_left = math.radians(225)
            angle_right = math.radians(315)
            spd = 16
            Bullet(cx - 25, top, damage=9,
                   speed_x=spd * math.cos(angle_left), speed_y=spd * math.sin(angle_left),
                   bullet_type='yellow_small_left')
            Bullet(cx + 25, top, damage=9,
                   speed_x=spd * math.cos(angle_right), speed_y=spd * math.sin(angle_right),
                   bullet_type='yellow_small_right')
        elif lvl == 4:
            Bullet(cx - 20, top, damage=10, bullet_type='yellow_main')
            Bullet(cx - 7, top, damage=5, bullet_type='yellow_small')
            Bullet(cx + 7, top, damage=5, bullet_type='yellow_small')
            Bullet(cx + 20, top, damage=10, bullet_type='yellow_main')
            spd = 16
            angle_left1 = math.radians(200)
            angle_left2 = math.radians(250)
            angle_right1 = math.radians(290)
            angle_right2 = math.radians(340)
            Bullet(cx - 25, top - 5, damage=9,
                   speed_x=spd * math.cos(angle_left1), speed_y=spd * math.sin(angle_left1),
                   bullet_type='yellow_small_left')
            Bullet(cx - 25, top + 5, damage=9,
                   speed_x=spd * math.cos(angle_left2), speed_y=spd * math.sin(angle_left2),
                   bullet_type='yellow_small_left')
            Bullet(cx + 25, top - 5, damage=9,
                   speed_x=spd * math.cos(angle_right1), speed_y=spd * math.sin(angle_right1),
                   bullet_type='yellow_small_right')
            Bullet(cx + 25, top + 5, damage=9,
                   speed_x=spd * math.cos(angle_right2), speed_y=spd * math.sin(angle_right2),
                   bullet_type='yellow_small_right')
        elif lvl == 5:
            Bullet(cx - 20, top, damage=10, bullet_type='yellow_main')
            Bullet(cx - 7, top, damage=5, bullet_type='yellow_small')
            Bullet(cx + 7, top, damage=5, bullet_type='yellow_small')
            Bullet(cx + 20, top, damage=10, bullet_type='yellow_main')

            spd = 16
            left_angles = [200, 220, 240]
            for ang in left_angles:
                rad = math.radians(ang)
                Bullet(cx - 25, top, damage=9,
                       speed_x=spd * math.cos(rad),
                       speed_y=spd * math.sin(rad),
                       bullet_type='yellow_small_left')
            right_angles = [300, 320, 340]
            for ang in right_angles:
                rad = math.radians(ang)
                Bullet(cx + 25, top, damage=9,
                       speed_x=spd * math.cos(rad),
                       speed_y=spd * math.sin(rad),
                       bullet_type='yellow_small_right')

    def shoot_blue(self):
        lvl = self.weapon_level_blue
        cx, top = self.rect.centerx, self.rect.top
        if lvl == 1:
            Bullet(cx - 20, top, damage=5, bullet_type='yellow_small', penetrate=0)
            Bullet(cx, top, damage=3, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 20, top, damage=5, bullet_type='yellow_small', penetrate=0)
        elif lvl == 2:
            Bullet(cx - 20, top, damage=5, bullet_type='yellow_main', penetrate=0)
            Bullet(cx - 7, top, damage=3, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 7, top, damage=3, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 20, top, damage=5, bullet_type='yellow_main', penetrate=0)
        elif lvl == 3:
            Bullet(cx - 20, top, damage=6, bullet_type='blue_large', penetrate=2)
            Bullet(cx - 7, top, damage=3, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 7, top, damage=3, bullet_type='blue_small', penetrate=1)
            Bullet(cx + 20, top, damage=6, bullet_type='blue_large', penetrate=2)
        elif lvl == 4:
            offsets = [-20, -7, 7, 20]
            for off in offsets:
                Bullet(cx + off, top, damage=6, bullet_type='blue_large', penetrate=2)
        elif lvl >= 5:
            Bullet(cx - 20, top, damage=6, bullet_type='blue_large', penetrate=2)
            now = pygame.time.get_ticks()
            if now - self.laser_shot_timer >= 150:
                self.laser_shot_timer = now
                LaserBeam(cx, top, frames=laser_frames)
            Bullet(cx + 20, top, damage=6, bullet_type='blue_large', penetrate=2)

    def activate_ult(self):
        if self.dying or self.ult_charges <= 0 or self.ultimate_active:
            return False
        if self.weapon_type == 'blue' and self.weapon_level_blue >= 1:
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
        if hasattr(powerup, 'current_color'):
            color = powerup.current_color
        else:
            color = powerup.type
        if color == 'yellow':
            self.weapon_type = 'yellow'
            if self.weapon_level_yellow < 5:
                self.weapon_level_yellow += 1
            else:
                self.activate_overload()
        elif color == 'blue':
            self.weapon_type = 'blue'
            if self.weapon_level_blue == 0:
                self.weapon_level_blue = 1
            elif self.weapon_level_blue < 5:
                self.weapon_level_blue += 1
            else:
                self.activate_overload()

    def activate_overload(self):
        cx, cy = self.rect.centerx, self.rect.top
        if self.weapon_type == 'yellow':
            for angle in range(0, 360, 30):
                rad = math.radians(angle)
                spd = 10
                Bullet(cx, cy, damage=300, speed_x=spd * math.cos(rad), speed_y=spd * math.sin(rad),
                       bullet_type='overload')
        else:
            for angle in range(0, 360, 30):
                rad = math.radians(angle)
                spd = 5
                OverloadBullet(cx, cy, speed_x=spd * math.cos(rad), speed_y=spd * math.sin(rad))


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
        else:
            self.image = pygame.Surface((10, 20))
            self.image.fill(WHITE)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_x = speed_x
        self.speed_y = speed_y
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
        all_enemies = list(rocks) + list(enemy1_group) + list(enemy2_group) + list(boss_group) + list(special_enemies) + list(enemy4_group)
        for enemy in all_enemies:
            if enemy in self.already_hit:
                continue
            enemy_rect = getattr(enemy, 'hitbox_rect', enemy.rect)
            if self.rect.colliderect(enemy_rect):
                enemy.take_damage(self.damage)
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
            scaled = pygame.transform.scale(f, (beam_width, beam_height))
            self.scaled_frames.append(scaled)
        self.image = self.scaled_frames[0]
        self.damage = 10
        self.lifetime = 300
        self.born_time = pygame.time.get_ticks()
        self.damage_enemies()
        all_sprites.add(self)
        bullets.add(self)

    def damage_enemies(self):
        all_enemies = list(rocks) + list(enemy1_group) + list(enemy2_group) + list(boss_group) + list(
            special_enemies) + list(enemy4_group)
        for enemy in all_enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.damage)

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
    """蓝色大招激光：伤害一次，存活0.6秒，使用三帧动画"""
    def __init__(self, x, player_top_y, beam_width, beam_height, frames):
        super().__init__()
        self.frames = frames
        self.frame_index = 0
        self.frame_duration = 100
        self.last_update = pygame.time.get_ticks()

        self.beam_width = beam_width
        self.beam_height = beam_height

        self.image = pygame.transform.scale(self.frames[0], (beam_width, beam_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = player_top_y
        self.rect.top = 0

        self.damage = 500
        self.lifetime = 600
        self.born_time = pygame.time.get_ticks()

        self.damage_enemies()

    def damage_enemies(self):
        all_enemies = (rocks.sprites() + enemy1_group.sprites() + enemy2_group.sprites() +
                       boss_group.sprites() + special_enemies.sprites() + enemy4_group.sprites())
        for enemy in all_enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.damage)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.born_time > self.lifetime:
            self.kill()
            return

        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            cx = self.rect.centerx
            bottom = self.rect.bottom
            self.image = pygame.transform.scale(self.frames[self.frame_index],
                                                (self.beam_width, self.rect.height))
            self.rect = self.image.get_rect()
            self.rect.centerx = cx
            self.rect.bottom = bottom
            self.rect.top = 0


class OverloadBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()
        self.original_image = overload2_img.copy()
        angle = math.degrees(math.atan2(speed_x, speed_y))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.damage = 200
        self.penetrate = -1
        all_sprites.add(self)
        bullets.add(self)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()


# 刷怪辅助函数
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


def spawn_enemy4(x_list):
    for x in x_list:
        e = Enemy4(x)
        all_sprites.add(e)
        enemy4_group.add(e)


def spawn_sp1(x):
    sp = EnemySp1(x)
    all_sprites.add(sp)
    special_enemies.add(sp)


def spawn_sp2(x):
    sp = EnemySp2(x)
    all_sprites.add(sp)
    special_enemies.add(sp)


def spawn_boss():
    boss = Boss1()
    all_sprites.add(boss)
    boss_group.add(boss)


def spawn_rock(x):
    r = Rock(x)
    all_sprites.add(r)
    rocks.add(r)


def spawn_rocks(x_list):
    for x in x_list:
        spawn_rock(x)


# 刷怪配置
stage_events = {
    STAGE_1: [
        (1000, lambda: spawn_sp1(350)), (1000, lambda: spawn_sp1(300)), (1000, lambda: spawn_sp1(250)),
        (1000, lambda: spawn_sp1(200)), (1000, lambda: spawn_sp1(150)), (1000, lambda: spawn_sp1(100)),
#(1000, lambda: spawn_rock(100)), (1000, lambda: spawn_enemy1([500])),
        #(2000, lambda: spawn_rock(800)),
        #(3000, lambda: spawn_rocks([150, 550])),
        #(4000, lambda: spawn_rock(100)),
        #(4200, lambda: spawn_rock(200)),
        #(4400, lambda: spawn_rock(300)),
        #(4600, lambda: spawn_rock(400)),
        #(4800, lambda: spawn_rock(500)),
        #(5000, lambda: spawn_rock(600)),
        #(5000, lambda: spawn_sp1(350)), (5000, lambda: spawn_sp1(300)), (5000, lambda: spawn_sp1(250)),
        #(5000, lambda: spawn_sp1(200)), (5000, lambda: spawn_sp1(150)), (5000, lambda: spawn_sp1(100)),
        #(5000, lambda: spawn_sp1(50)),
        #(7000, lambda: spawn_enemy1([200])),
        #(7000, lambda: spawn_enemy1([300])),
        #(7200, lambda: spawn_enemy1([450])),
        #(7400, lambda: spawn_enemy1([500])),
        #(7600, lambda: spawn_enemy1([550])),
        #(7800, lambda: spawn_enemy1([600])),
        #(8000, lambda: spawn_enemy1([650])),
        #(9000, lambda: spawn_rocks([0, 100, 200, 300, 400, 500, 600, 700])),
        #(9500, lambda: spawn_rocks([0, 100, 200, 300, 400, 500, 600, 700])),
        #(11000, lambda: spawn_sp2(200)),
        #(13000, lambda: spawn_enemy1([100, 250, 400, 550])),
        #(17000, lambda: spawn_sp1(600)),
        #(19000, lambda: spawn_rocks([200, 500])),
    ],
    STAGE_2: [
        (3000, lambda: spawn_enemy2([150])),
        (5000, lambda: spawn_sp1(200)),
        (7000, lambda: spawn_enemy2([200, 350, 500])),
        (9000, lambda: spawn_enemy1([250, 450])),
        (11000, lambda: spawn_sp2(WIDTH // 2)),
        (13000, lambda: spawn_enemy2([100, 300, 500])),
        (15000, lambda: spawn_enemy1([150, 250, 350, 450, 550])),
        (17000, lambda: spawn_sp1(WIDTH // 2)),
        (19000, lambda: spawn_enemy2([200, 400])),
    ],
    STAGE_3: [
        (1000, lambda: spawn_enemy1([100, 200, 300, 400, 500])),
        (3000, lambda: spawn_enemy2([150, 250, 350, 450])),
        (5000, lambda: spawn_sp1(WIDTH // 2)),
        (7000, lambda: spawn_enemy1([200, 300, 400])),
        (9000, lambda: spawn_enemy2([100, 600])),
        (11000, lambda: spawn_sp2(WIDTH // 2)),
        (13000, lambda: spawn_enemy1([150, 550])),
        (15000, lambda: spawn_enemy2([200, 350, 500])),
        (17000, lambda: spawn_sp1(WIDTH // 2)),
        (19000, lambda: spawn_enemy1([100, 250, 400, 550])),
    ],
    STAGE_4: [
        (1000, lambda: spawn_enemy4([350])),
        (3000, lambda: spawn_enemy1([100, 200, 300, 400, 500, 600])),
        (5000, lambda: spawn_sp1(WIDTH // 2)),
        (7000, lambda: spawn_enemy2([150, 250, 350, 450])),
        (9000, lambda: spawn_enemy4([175, 525])),
        (11000, lambda: spawn_sp2(WIDTH // 2)),
        (13000, lambda: spawn_enemy1([200, 300, 400])),
        (15000, lambda: spawn_enemy2([100, 600])),
        (17000, lambda: spawn_sp1(WIDTH // 2)),
        (19000, lambda: spawn_enemy4([175, 525])),
    ],
    STAGE_BOSS: [],
    STAGE_WIN: [],
}

# 游戏主循环
player = Player()
all_sprites.add(player)
bg_offset = (player.rect.centerx - WIDTH / 2) * -0.12
last_bg_offset = bg_offset

triggered_events = {stage: [] for stage in STAGE_DURATION.keys()}

running = True
boss_spawned = False

while running:
    clock.tick(FPS)
    now_time = pygame.time.get_ticks()
    stage_elapsed = now_time - stage_start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    space_pressed = keys[pygame.K_SPACE]
    if space_pressed and not space_was_pressed and not player.dying:
        player.activate_ult()
    space_was_pressed = space_pressed

    if game_stage in stage_events:
        events = stage_events[game_stage]
        for idx, (time_ms, callback) in enumerate(events):
            if idx not in triggered_events[game_stage] and stage_elapsed >= time_ms:
                callback()
                triggered_events[game_stage].append(idx)

    if game_stage == STAGE_BOSS and not boss_spawned:
        spawn_boss()
        boss_spawned = True

    if game_stage != STAGE_WIN:
        duration = STAGE_DURATION.get(game_stage, 0)
        if duration > 0 and stage_elapsed >= duration:
            if game_stage < STAGE_BOSS:
                game_stage += 1
                stage_start_time = now_time
                triggered_events[game_stage] = []
            elif game_stage == STAGE_BOSS:
                pass

    if not player.dying and not player.invincible:
        hit_bullets = pygame.sprite.spritecollide(player, enemy_bullets, True, pygame.sprite.collide_circle)
        for bullet in hit_bullets:
            player.take_damage(bullet.damage, direct_kill=False)

    if not player.dying and not player.invincible:
        if pygame.sprite.spritecollide(player, rocks, False, pygame.sprite.collide_circle):
            player.take_damage(0, direct_kill=True)
        if pygame.sprite.spritecollide(player, enemy1_group, False, pygame.sprite.collide_circle):
            player.take_damage(0, direct_kill=True)
        if pygame.sprite.spritecollide(player, enemy2_group, False, pygame.sprite.collide_circle):
            player.take_damage(0, direct_kill=True)
        if pygame.sprite.spritecollide(player, special_enemies, False, pygame.sprite.collide_circle):
            player.take_damage(0, direct_kill=True)
        for e4 in enemy4_group:
            if player.rect.colliderect(e4.hitbox_rect):
                player.take_damage(0, direct_kill=True)
                break
        if pygame.sprite.spritecollide(player, boss_group, False, pygame.sprite.collide_circle):
            player.take_damage(0, direct_kill=True)

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
            player.respawn()

    screen.fill(BLACK)
    bg_offset = (player.rect.centerx - WIDTH / 2) * -0.12 if not player.dying else bg_offset
    offset_change = bg_offset - last_bg_offset

    for rock in rocks: rock.move_with_bg(offset_change)
    for e1 in enemy1_group: e1.move_with_bg(offset_change)
    for e2 in enemy2_group: e2.move_with_bg(offset_change)
    for eb in enemy_bullets: eb.move_with_bg(offset_change)
    for sp in special_enemies: sp.move_with_bg(offset_change)
    for pw in powerups: pw.move_with_bg(offset_change)
    for e4 in enemy4_group: e4.move_with_bg(offset_change)

    last_bg_offset = bg_offset

    bg1_y += bg_speed
    bg2_y += bg_speed
    if bg1_y >= HEIGHT: bg1_y = -HEIGHT
    if bg2_y >= HEIGHT: bg2_y = -HEIGHT

    screen.blit(background_img1, (bg_offset - MAX_BG_OFFSET, bg1_y))
    screen.blit(background_img1, (bg_offset - MAX_BG_OFFSET, bg2_y))
    all_sprites.draw(screen)

    icon_spacing = 5
    start_x = 10
    start_y = HEIGHT - 90
    for i in range(player.lives):
        screen.blit(life_icon_img, (start_x + i * (LIFE_ICON_SIZE + icon_spacing), start_y))

    hp_label = font.render("HP:", True, WHITE)
    screen.blit(hp_label, (10, HEIGHT - 60))
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
    if player.ult_charges > max_ult_icons:
        extra_text = font.render(f"+{player.ult_charges - max_ult_icons}", True, WHITE)
        screen.blit(extra_text, (ult_start_x + max_ult_icons * (ULT_ICON_SIZE + ult_spacing) + 5, ult_start_y))

    if game_stage == STAGE_WIN:
        win_text = font.render("VICTORY! 10 seconds to exit...", True, WHITE)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

    if game_stage == STAGE_WIN and stage_elapsed >= STAGE_DURATION[STAGE_WIN]:
        running = False

    if game_over:
        if not any(isinstance(s, PlayerExplosion) for s in all_sprites):
            running = False

pygame.quit()