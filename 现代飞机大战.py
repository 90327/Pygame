import sys
import main
import pygame
import traceback


pygame.init()
size = width, height = 512, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TylerXixi                  ------------现代飞机大战------------')
clock = pygame.time.Clock()
cover_image = pygame.image.load('image\\cover\\cover_plus.png').convert_alpha()


screen.blit(cover_image, (0, 0))
pygame.display.flip()
clock.tick(60)

if __name__ == '__main__':
    pygame.time.delay(3 * 1000)
try:
    main.main()
except SystemExit:
    pass
except:
    traceback.print_exc()
    input()
