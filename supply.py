import pygame
from random import *


class BulletSupply(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image\\boom\\bullet_fly.png')
        self.width, self.height = size[0], size[1]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), 100
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), 100


class BombSupply(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image\\boom\\bomb_fly.png')
        self.rect = self.image.get_rect()
        self.width, self.height = size[0], size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), 100
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), 100


class LifeSupply(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image\\boom\\fly_life.png')
        self.width, self.height = size[0], size[1]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), 100
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), 100
