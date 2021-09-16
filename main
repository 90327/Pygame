import sys
import time
import traceback

import pygame.mixer
from pygame.locals import *

import bullet
import enemyplan
import myplan
import supply
from enemyplan import *

# 初始化
pygame.init()
pygame.mixer.init()

# 帧数对象创建
clock = pygame.time.Clock()

# 设置屏幕大小
size = width, height = 512, 900
screen = pygame.display.set_mode(size)

# 设置标题
pygame.display.set_caption('TylerXixi                  ------------现代飞机大战------------')

# 载入图片
# 背景图片
background = pygame.image.load('image\\background\\1.jpg').convert_alpha()
# ICO游戏图标
ico = pygame.image.load('image\\ICO\\J20.ico')
pygame.display.set_icon(ico)
# 暂停时图片
people_pause_image = pygame.image.load('image\\Pause\\j20_gaitubao_656x464.png').convert_alpha()
font_image = pygame.image.load('image\\Pause\\font22.png').convert_alpha()

# 载入游戏音效
# 主背景音乐
pygame.mixer.music.load('Wav\\back music\\backmusci.mp3')
pygame.mixer.music.set_volume(0.03)
# 达到四级背景音乐
level4_backmusic = pygame.mixer.Sound('Wav\\back music\\4级BGM.mp3')
level4_backmusic.set_volume(0.1)
# 达到6级背景音乐
level6_backmusic = pygame.mixer.Sound("Wav\\back music\\6级BGM.mp3")
level6_backmusic.set_volume(0.2)

supperbig_sound = pygame.mixer.Sound('Wav\\sound\\supperbig_sound.ogg')
supperbig_sound.set_volume(0.03)
big_sound = pygame.mixer.Sound('Wav\\sound\\big_sound.ogg')
big_sound.set_volume(0.1)
mid_sound = pygame.mixer.Sound('Wav\\sound\\mid_sound.ogg')
mid_sound.set_volume(0.03)
small_sound = pygame.mixer.Sound('Wav\\sound\\small_sound.ogg')
small_sound.set_volume(0.03)
appear_bigplan = pygame.mixer.Sound('Wav\\sound\\大飞机来咯-1_2.ogg')
appear_bigplan.set_volume(0.05)
die_Myplan = pygame.mixer.Sound('Wav\\sound\\哦豁-.ogg')
die_Myplan.set_volume(0.05)
GameOver_plan = pygame.mixer.Sound('Wav\\sound\\游戏结束-.ogg')
GameOver_plan.set_volume(0.05)
boom_sound = pygame.mixer.Sound('Wav\\sound\\核弹.ogg')
boom_sound.set_volume(0.5)
supply_appear = pygame.mixer.Sound('Wav\\sound\\补给箱已经-.ogg')
supply_appear.set_volume(0.05)
get_bomb = pygame.mixer.Sound('Wav\\sound\\获得核弹.ogg')
get_bomb.set_volume(0.05)
too_much_bomb = pygame.mixer.Sound('Wav\\sound\\最大炸弹量.ogg')
too_much_bomb.set_volume(0.05)
too_much_life = pygame.mixer.Sound('Wav\\sound\\最大生命值.ogg')
too_much_life.set_volume(0.05)
get_bullet = pygame.mixer.Sound('Wav\\sound\\获得子弹.ogg')
get_bullet.set_volume(0.05)
get_life = pygame.mixer.Sound('Wav\\sound\\获得生命.ogg')
get_life.set_volume(0.05)
launch_bullet = pygame.mixer.Sound('Wav\\sound\\普通子弹发射.ogg')
launch_bullet.set_volume(0.01)
# 等级音效
level2_sound = pygame.mixer.Sound('Wav\\sound\\二级.ogg')
level2_sound.set_volume(0.1)
level3_sound = pygame.mixer.Sound('Wav\\sound\\三级_1_1.ogg')
level3_sound.set_volume(0.1)
level4_sound = pygame.mixer.Sound('Wav\\sound\\四级_1_1.ogg')
level4_sound.set_volume(0.1)
level5_sound = pygame.mixer.Sound('Wav\\sound\\五级_1_1.ogg')
level5_sound.set_volume(0.1)
level6_sound = pygame.mixer.Sound('Wav\\sound\\六级_1_1.ogg')
level6_sound.set_volume(0.1)


# 血条颜色定义
BLACK = (0, 0, 0)
RED = (224, 30, 30)
GREEN = (24, 220, 24)
WHITE = (255, 255, 255)
Font_color = (191, 239, 255)


# 添加小型敌机
def add_small_enemy(group1, group2, num):
    for i in range(num):
        # 实例化敌方飞机
        e1 = enemyplan.SmallPlan(size)
        group1.add(e1)
        group2.add(e1)


# 添加中型敌机
def add_mid_enemy(group1, group2, num):
    for i in range(num):
        e2 = enemyplan.MidPlan(size)
        group1.add(e2)
        group2.add(e2)


# 添加大型敌机
def add_big_enemy(group1, group2, num):
    for i in range(num):
        e3 = enemyplan.BigPlan(size)
        group1.add(e3)
        group2.add(e3)


# 定义敌机的速度
def inc_speed(target, inc):
    for each in target:
        each.speed += inc


def main():
    # 整除对象
    delay = 100

    # 等级设置
    level = 1

    # 分数设置
    score = 0
    # 分数字体设置
    score_font = pygame.font.Font('Font\\HYZhuZiMuTouRenW.ttf', 40)

    # 控制图片状态
    switch_image = True

    # 循环状态
    running = True

    # 控制暂停状态
    pause = False

    # 控制声音状态
    voice_pause = False

    # 控制文件打开次数
    recorded = False

    # 导入暂停图片
    pause_nor_image = pygame.image.load('image\\Pause\\not pause_white.png').convert_alpha()
    pause_pressd_image = pygame.image.load('image\\Pause\\not pause_gray.png').convert_alpha()
    resumer_nor_image = pygame.image.load('image\\Pause\\resumer_white.png').convert_alpha()
    resumer_pressd_image = pygame.image.load('image\\Pause\\resumer_gray.png').convert_alpha()

    # 导入声音图片
    voice_image_blue = pygame.image.load('image\\voice\\voice (1)_gaitubao_66x66.png').convert_alpha()
    voice_image_green = pygame.image.load('image\\voice\\voice (2)_gaitubao_66x66.png').convert_alpha()
    pause_voice_image_blue = pygame.image.load('image\\voice\\pause_voice (1)_gaitubao_66x66.png').convert_alpha()
    pause_voice_image_green = pygame.image.load('image\\voice\\pause_voice (2)_gaitubao_66x66.png').convert_alpha()

    # 导入结束、重开、GameOver、logo图片
    end_image = pygame.image.load('image\\restart\\G2.png').convert_alpha()
    end_rect = end_image.get_rect()
    again_image = pygame.image.load("image\\restart\\重新开始.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("image\\restart\\结束游戏.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()
    logo_image = pygame.image.load('image\\restart\\ico.png').convert_alpha()
    logo_font = pygame.image.load('image\\restart\\LogoFont.png').convert_alpha()
    # 结束字体
    gameover_font = pygame.font.Font("Font\\华文圆体 REGULAR.TTF", 48)

    # 导入复活图片
    reset_life = pygame.image.load('image\\life\\Rese_life.png').convert_alpha()
    reset_font_image = pygame.image.load('image\\life\\reset_font_life.png').convert_alpha()

    # 导入生命UI图标
    life_image = pygame.image.load('image\\boom\\LIFE.png').convert_alpha()
    # 获取生命图标矩形位置
    life_rect = life_image.get_rect()
    # 设置生命剩余字体
    life_font = pygame.font.Font('Font\\华文圆体 REGULAR.TTF', 45)
    # 生命数量
    life_num = 3

    # 导入炸弹UI图标
    boom_image = pygame.image.load('image\\boom\\BOOM.png').convert_alpha()
    # 获取炸弹的矩形位置
    boom_rect = boom_image.get_rect()
    # 设置炸弹剩余字体
    boom_font = pygame.font.Font('Font\\华文圆体 REGULAR.TTF', 45)
    # 设置炸弹的数量
    boom_num = 3

    # 实例化补给包
    # 子弹补给
    bullet_supply = supply.BulletSupply(size)
    # 核弹补给
    bomb_supply = supply.BombSupply(size)
    # 生命补给
    life_supply = supply.LifeSupply(size)

    # 设置每40秒放发任意一个补给包
    supply_timer = USEREVENT
    pygame.time.set_timer(supply_timer, 40 * 1000)

    # 设置超级子弹的发射时间
    double_bullet_timer = USEREVENT + 1

    # 设置无敌时间
    invincible_timer = USEREVENT + 2

    # 标准是否使用超级子弹
    is_double_bullet = False

    # 获取pause图片的矩形
    paused_rect = pause_pressd_image.get_rect()
    # 初始化图片的位置
    paused_rect.left, paused_rect.top = width - paused_rect.width - 5, 5
    # 默认显示图标
    paused_image = pause_nor_image

    # 获取声音矩形图像
    voice_rect = voice_image_blue.get_rect()
    # 初始化图像位置
    voice_rect.left, voice_rect.top = width - voice_rect.width - 5, 75
    # 默认显示图
    voice_image = voice_image_blue

    #
    # 播放背景音乐:
    pygame.mixer.music.play(-1)

    # 生成我方飞机
    me = myplan.MyPlan(size)

    # 生成普通子弹  设置添加子弹的列表
    bullet1 = []
    # 添加图片索引
    bullet1_index = 0
    # 添加子弹数量
    bullet1_nums = 7
    # 将子弹迭代拿出并添加到列表
    for i in range(bullet1_nums):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    # 生成超级子弹
    # 设置添加子弹的列表
    bullet2 = []
    # 添加图片索引
    bullet2_index = 0
    # 添加子弹数量
    bullet2_nums = 12
    # 将子弹迭代拿出并添加到列表
    for i in range(bullet2_nums//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx-55, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+20, me.rect.centery)))

    # 生成敌方飞机
    enemys = pygame.sprite.Group()
    # 生成小型敌机
    small_enemy = pygame.sprite.Group()
    add_small_enemy(small_enemy, enemys, 14)
    # 生成中型飞机
    mid_enemy = pygame.sprite.Group()
    add_mid_enemy(mid_enemy, enemys, 6)
    # 生成大型飞机
    big_enemy = pygame.sprite.Group()
    add_big_enemy(big_enemy, enemys, 2)

    # 中弹图片索引
    small_destory_index = 0
    mid_destory_index = 0
    big_destory_index = 0
    me_destory_index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    pause = not pause
                    # 暂停游戏所有音效
                    if pause:
                        pygame.time.set_timer(supply_timer, 0)

                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(supply_timer, 40*1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if pause:
                        paused_image = resumer_pressd_image
                    else:
                        paused_image = pause_pressd_image

                else:
                    if pause:
                        paused_image = resumer_nor_image
                    else:
                        paused_image = pause_nor_image

                # 声音控制
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and voice_rect.collidepoint(event.pos):
                    voice_pause = not voice_pause
            elif event.type == MOUSEMOTION:
                if voice_rect.collidepoint(event.pos):
                    if voice_pause:
                        voice_image = pause_pressd_image
                    else:
                        voice_image = voice_image_green

                else:
                    if voice_pause:
                        voice_image = pause_voice_image_blue
                    else:
                        voice_image = voice_image_blue

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if boom_num:
                        # 炸弹减一
                        boom_num -= 1
                        # 播放炸弹音效
                        boom_sound.play()
                        for each in enemys:
                            # 如果敌机在底部的上面将全部毁灭
                            if each.rect.bottom > 0:
                                each.active = False
            # 判断补给箱是否触发
            elif event.type == supply_timer:
                supply_appear.play()
                main_value = randint(0, 20)
                if main_value % 3 == 0:
                    bomb_supply.reset()
                if main_value % 3 == 1:
                    life_supply.reset()
                if main_value % 3 == 2:
                    bullet_supply.reset()

            elif event.type == double_bullet_timer:
                is_double_bullet = False
                pygame.time.set_timer(double_bullet_timer, 0)

            elif event.type == invincible_timer:
                me.invincible = False
                pygame.time.set_timer(invincible_timer, 0)

        # 等级难度提升
        # 二级难度
        if level == 1 and score > 30000:
            level = 2
            level2_sound.play()
            # 增加小型敌机3 中型2， 大型1
            add_small_enemy(small_enemy, enemys, 3)
            add_mid_enemy(mid_enemy, enemys, 2)
            add_big_enemy(big_enemy, enemys, 1)
            # 增加小型敌机速度
            inc_speed(small_enemy, 1)

        # 三级难度
        elif level == 2 and score > 100000:
            level = 3
            level3_sound.play()
            # 增加小型敌机4， 中型3， 大型2
            add_small_enemy(small_enemy, enemys, 4)
            add_mid_enemy(mid_enemy, enemys, 3)
            add_big_enemy(big_enemy, enemys, 2)
            # 增加小型, 中型敌机速度
            inc_speed(small_enemy, 1)

        # 四级难度
        elif level == 3 and score > 300000:
            level = 4
            level4_sound.play()
            pygame.mixer.music.pause()
            level4_backmusic.play(-1)
            pygame.time.set_timer(supply_timer, 30 * 1000)
            # 增加小型敌机6， 中型5， 大型3
            add_small_enemy(small_enemy, enemys, 6)
            add_mid_enemy(mid_enemy, enemys, 5)
            add_big_enemy(big_enemy, enemys, 3)
            # 增加小型, 中型敌机速度
            inc_speed(small_enemy, 1)

        # 五级难度
        elif level == 4 and score > 600000:
            level = 5
            level5_sound.play()
            # 增加小型敌机8， 中型7， 大型4
            add_small_enemy(small_enemy, enemys, 8)
            add_mid_enemy(mid_enemy, enemys, 7)
            add_big_enemy(big_enemy, enemys, 4)
            # 增加小型, 中型敌机速度
            inc_speed(small_enemy, 2)

        # 六级难度
        elif level == 5 and score > 1000000:
            level = 6
            level6_sound.play()
            level4_backmusic.stop()
            level6_backmusic.play(-1)
            # 增加小型敌机10， 中型9， 大型6
            add_small_enemy(small_enemy, enemys, 10)
            add_mid_enemy(mid_enemy, enemys, 9)
            add_big_enemy(big_enemy, enemys, 6)
            # 增加小型, 中型敌机速度
            inc_speed(small_enemy, 2)
            inc_speed(mid_enemy, 1)


        # 绘制游戏背景
        screen.blit(people_pause_image, (0, 250))
        screen.blit(font_image, (0, 550))

        if life_num and not pause:
            # 检测用户键盘操作
            key_button = pygame.key.get_pressed()
            if key_button[K_w] or key_button[K_UP]:
                me.moveup()
            if key_button[K_s] or key_button[K_DOWN]:
                me.movedown()
            if key_button[K_a] or key_button[K_LEFT]:
                me.moveleft()
            if key_button[K_d] or key_button[K_RIGHT]:
                me.moveright()
            screen.blit(background, (0, 0))

            # 绘制核弹并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                # 检测是否获得
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb.play()
                    if boom_num < 3:
                        boom_num += 1
                    if boom_num >= 3:
                        too_much_bomb.play()
                    bomb_supply.active = False

            # 绘制生命并检测是否获得
            if life_supply.active:
                life_supply.move()
                screen.blit(life_supply.image, life_supply.rect)
                # 检测是否获得
                if pygame.sprite.collide_mask(life_supply, me):
                    get_bomb.play()
                    if life_num < 3:
                        life_num += 1
                    if life_num >= 3:
                        too_much_life.play()
                    life_supply.active = False

            # 绘制超级子弹
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                # 检测是否获得
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet.play()
                    # 发射超级子弹
                    is_double_bullet = True
                    pygame.time.set_timer(double_bullet_timer, 20 * 1000)
                    bullet_supply.active = False

            # 发射子弹 delay % 10 就是限制子弹为10帧/s
            if not (delay % 10):
                launch_bullet.play()
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-55, me.rect.centery))
                    bullets[bullet2_index+1].reset((me.rect.centerx+20, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % bullet2_nums
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset((me.rect.centerx-2.5, me.rect.centery))
                    bullet1_index = (bullet1_index + 1) % bullet1_nums

            # 检测子弹击中敌人
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemys, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in big_enemy or e in mid_enemy:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
            # 绘制大型敌机
            for each in big_enemy:
                if each.active:
                    # 初速度
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    # 绘制大型敌机血量底槽
                    pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top - 5),
                                                    (each.rect.right, each.rect.top - 5), 4)
                    # 绘制大型飞机击中时血量
                    # 计算当时的血量
                    energy_count = each.energy / enemyplan.BigPlan.energy
                    # 如果血量大于百分之二十绘制绿色 否则绘制红色
                    if energy_count > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    # 绘制敌机被击中的当时血量
                    pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5),
                                                           (each.rect.left + each.rect.width * energy_count,
                                                            each.rect.top - 5), 4)

                    # 添加出场音效
                    if each.rect.bottom == -100:
                        appear_bigplan.play()
                else:
                    # 飞机毁灭播放
                    if not (delay % 3):
                        if big_destory_index == 0:
                            big_sound.play()
                        screen.blit(each.destory_images[big_destory_index], each.rect)
                        big_destory_index = (big_destory_index + 1) % 9
                        if big_destory_index == 0:
                            score += 13140
                            each.reset()

            # 绘制中型敌机
            for each in mid_enemy:
                if each.active:
                    # 初速度
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    # 绘制中型敌机血量底槽
                    pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 3)
                    # 绘制中型飞机击中时血量
                    # 计算当时的血量
                    energy_count = each.energy / enemyplan.MidPlan.energy

                    # 如果血量大于百分之二十绘制绿色 否则绘制红色
                    if energy_count > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    # 绘制敌机被击中的当时血量
                    pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_count,
                                      each.rect.top - 5), 3)
                else:
                    if not (delay % 3):
                        # 毁灭图像播放
                        if mid_destory_index == 0:
                            mid_sound.play()
                        screen.blit(each.destory_images[mid_destory_index], each.rect)
                        mid_destory_index = (mid_destory_index + 1) % 6
                        if mid_destory_index == 0:
                            score += 5200
                            each.reset()

            # 绘制小型敌机
            for each in small_enemy:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not (delay % 3):
                        # 毁灭播放图像音频
                        if small_destory_index == 0:
                            small_sound.play()
                        screen.blit(each.destory_images[small_destory_index], each.rect)
                        small_destory_index = (small_destory_index + 1) % 4
                        if small_destory_index == 0:
                            score += 520
                            each.reset()
            # 我方飞机碰撞检测
            enemys_down = pygame.sprite.spritecollide(me, enemys, False, pygame.sprite.collide_mask)
            if enemys_down and not me.invincible:
                me.active = False
                for e in enemys_down:
                    e.active = False

            # 绘制我方飞机
            if me.active:
                if switch_image:
                    screen.blit(me.image, me.rect)
                else:
                    screen.blit(me.image1, me.rect)
            else:
                # 毁灭图像播放
                if me_destory_index == 0:
                    die_Myplan.play()
                screen.blit(me.destory_image[me_destory_index], me.rect)
                me_destory_index = (me_destory_index + 1) % 4
                if me_destory_index == 0:
                    # 生命值-1
                    life_num -= 1

                    # 复活
                    me.reset()
                    pygame.time.set_timer(invincible_timer, 3 * 1000)
                    for i in range(life_num):
                        if not (delay % 1):
                            screen.blit(reset_font_image, me.rect)
            # 绘制炸弹UI
            boom_text = boom_font.render(' x %d ' % boom_num, True, WHITE)
            text_rect = boom_text.get_rect()
            screen.blit(boom_image, (5, 150))
            screen.blit(boom_text, (75, 150))

            # 绘制生命UI
            life_text = life_font.render(' x %d' % life_num, True, WHITE)
            text_rect = life_text.get_rect()
            screen.blit(life_image, (5, 65))
            screen.blit(life_text, (75, 65))
            # 将分数通过字符串添加到surface对象
            score_text = score_font.render('分数: %s' % str(score), True, WHITE)
            # 绘制分数
            screen.blit(score_text, (10, 20))

        elif life_num == 0:
            screen.blit(background, (0, 0))
            # 游戏结束背景音乐关闭
            pygame.mixer.music.stop()
            # 停止全部音效
            pygame.mixer.stop()
            # 停止发放补给箱
            pygame.time.set_timer(supply_timer, 0)

            # 用于存写历史记录
            if not recorded:
                recorded = True
                # 读取历史最高得分
                with open("游戏历史记录.txt", "r") as f:
                    record_score = int(f.read())
                # 判断当前分数是否高于游戏历史最高记录
                if score > record_score:
                    with open("游戏历史记录.txt", "w") as f:
                        f.write(str(score))

            # 绘制结束画面
            record_score_text = score_font.render("最高分 : %d" \
                                                  % record_score, True, (255, 255, 255))
            screen.blit(record_score_text, (0, 0))


            gameover_text1 = gameover_font.render("最终得分", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)

            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                (width - gameover_text2_rect.width) // 2, \
                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, (190, 355))

            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, \
                gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, \
                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 绘制GAMEOVER字体
            screen.blit(end_image, (100, 110))

            # 绘制LOGO
            # LOGO
            screen.blit(logo_image, (10, 810))
            # Font
            screen.blit(logo_font, (110, 802))

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:

                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()

                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                        again_rect.top < pos[1] < again_rect.bottom:

                    # 调用main函数，重新开始游戏
                    main()

                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:

                    # 退出游戏
                    pygame.quit()
                    sys.exit()

        # 绘制暂停按钮
        screen.blit(paused_image, paused_rect)
        # 绘制声音按钮
        screen.blit(voice_image, voice_rect)

        if not(delay % 1):
            switch_image = not switch_image
        delay -= 1
        if not delay:
            delay = 100

        # 游戏图像翻转
        pygame.display.flip()
        # 帧率限制
        clock.tick(60)


