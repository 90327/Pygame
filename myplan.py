import pygame


# 创建飞机类并初始化
class MyPlan(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        # 加载飞机
        self.image = pygame.image.load('image\\Myplan\\2.png').convert_alpha()
        self.image1 = pygame.image.load('image\\Myplan\\J20_2.png').convert_alpha()
        self.destory_image = []
        self.destory_image.extend([pygame.image.load('image\\blast\\small_blast\\1.1.png'),
                                   pygame.image.load('image\\blast\\small_blast\\2.1.png'),
                                   pygame.image.load('image\\blast\\small_blast\\3.2.png'),
                                   pygame.image.load('image\\blast\\small_blast\\4.3.png')])
        # 获取矩形位置
        self.rect = self.image.get_rect()
        # 赋值大小
        self.width, self.height = size[0], size[1]
        # 设置像素块为10
        self.speed = 10
        # 控制碰撞状态
        self.active = True
        # 控制无敌状态
        self.invincible = False
        # 初始化飞机位置
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height
        # 检测图像空白区域是否有碰撞
        self.mask = pygame.mask.from_surface(self.image)

    def moveup(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def movedown(self):
        if self.rect.bottom < self.height - 0:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 0

    def moveleft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveright(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height
        self.active = True
        self.invincible = True
