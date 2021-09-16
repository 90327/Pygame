import pygame
from random import *


# 小型飞机
class SmallPlan(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        # 载入小型飞机图像
        self.image = pygame.image.load('image\\Enemyplan\\F16.png').convert_alpha()
        # 载入飞机爆炸效果图像
        self.destory_images = []
        self.destory_images.extend([pygame.image.load('image\\blast\\small_blast\\0.1 (1).png').convert_alpha(),
                                    pygame.image.load('image\\blast\\small_blast\\0.1 (2).png').convert_alpha(),
                                    pygame.image.load('image\\blast\\small_blast\\0.1 (3).png').convert_alpha(),
                                    pygame.image.load('image\\blast\\small_blast\\0.1 (3).png').convert_alpha(),
                                    pygame.image.load('image\\blast\\small_blast\\0.1 (4).png').convert_alpha(),
                                    pygame.image.load('image\\blast\\small_blast\\0.1 (4).png').convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = size[0], size[1]
        self.speed = 2
        # 检测是否被子弹击毁
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        # 检测空白区域是否有碰撞
        self.mask = pygame.mask.from_surface(self.image)

    # 定义移动方法
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # 重新初始化图像位置
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)


# 中型飞机
class MidPlan(pygame.sprite.Sprite):
    # 设置敌机的血量
    energy = 10

    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image\\Enemyplan\\mid.png').convert_alpha()
        self.image_hit = pygame.image.load('image\\Enemyplan\\mid_hit (2).png').convert_alpha()
        self.destory_images = []
        self.destory_images.extend([pygame.image.load('image\\blast\\mid_blast\\1.1.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\mid_blast\\2.1.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\mid_blast\\3.1.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\mid_blast\\3.2.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\mid_blast\\4.1.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\mid_blast\\4.3.png').convert_alpha()])

        self.rect = self.image.get_rect()
        self.width, self.height = size[0], size[1]
        self.speed = 1
        # 检测是否被子弹击毁
        self.active = True
        # 检测子弹击中状态
        self.hit = False
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)
        # 检测空白区域是否有碰撞
        self.mask = pygame.mask.from_surface(self.image)
        # 用类来引用变量
        self.energy = MidPlan.energy

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MidPlan.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)


class BigPlan(pygame.sprite.Sprite):
    # 设置大型敌机的血量
    energy = 25

    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image\\Enemyplan\\big.png').convert_alpha()
        self.image_hit = pygame.image.load('image\\Enemyplan\\big_hit.png').convert_alpha()
        self.destory_images = []
        self.destory_images.extend([pygame.image.load('image\\blast\\big_blast\\1.1.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\big_blast\\1.2.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\big_blast\\2.1.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\big_blast\\2.2.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\big_blast\\3.1.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\big_blast\\3.2.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\big_blast\\4.1.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\big_blast\\4.2.png').convert_alpha(),
                                   pygame.image.load('image\\blast\\big_blast\\4.3.png').convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = size[0], size[1]
        self.speed = 1
        # 检测是否被子弹击毁
        self.active = True
        # 检测子弹击中状态
        self.hit = False
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
            randint(-15 * self.height, -5 * self.height)
        # 检测空白区域是否有碰撞
        self.mask = pygame.mask.from_surface(self.image)
        # 用类的方式引用变量
        self.energy = BigPlan.energy

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigPlan.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
            randint(-15 * self.height, -5 * self.height)
