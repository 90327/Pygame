import pygame


# 定义普通子弹
class Bullet1(pygame.sprite.Sprite):
    # 初始化 并给一个位置变量
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # 载入图片
        self.image = pygame.image.load('image\\bullet\\bullet_1.1.png').convert_alpha()
        # 设置子弹状态
        self.active = False
        # 获取子弹图像的矩形位置
        self.rect = self.image.get_rect()
        # 将子弹矩形位置赋值给变量位置
        self.rect.left, self.rect.top = position
        self.speed = 12
        # 检测图像空白区域并标记
        self.mask = pygame.mask.from_surface(self.image)

    # 定义移动
    def move(self):
        # 判断子弹矩形图像是否超出top
        self.rect.top -= self.speed
        # 子弹超出边界后给子弹状态变参
        if self.rect.top < 0:
            self.active = False

    # 定义重启方法
    def reset(self, position):
        # 参数为True后初始化子弹的矩形位置
        self.rect.left, self.rect.top = position
        # 将子弹状态变参
        self.active = True


# 定义超级子弹
class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image\\bullet\\bullet_2.png').convert_alpha()
        self.rect = self.image.get_rect()
        # 设置子弹状态
        self.active = False
        # 设置子弹的速度
        self.speed = 16
        # 设置空白区域标记
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    # 定义子弹重置
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
