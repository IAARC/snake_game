import pygame
from sys import exit

pygame.init()

x = 0
y = 0
dt = 0.1
px_of_square = 306
keep_game = True

clock = pygame.time.Clock()
snake_head_img = pygame.image.load('lib/snake_head.jpeg')
snake_head_img = pygame.transform.scale(snake_head_img, (snake_head_img.get_width() * 1/10,
                                        snake_head_img.get_height() * 1/10))


screen = pygame.display.set_mode((px_of_square,px_of_square))
pygame.display.set_caption('Snake Game')

while keep_game:

    keys = pygame.key.get_pressed()
    screen.fill((0,0,0))
    screen.blit(snake_head_img, (x,y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if keys[pygame.K_DOWN]:
        print('hello')
        y += 34/60
    elif keys[pygame.K_UP]:
        y -= 34/60
    elif keys[pygame.K_LEFT]:
        x -= 34/60
    else:
        x += 34/60


    pygame.display.flip()
    clock.tick(60)