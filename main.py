import pygame
from lib.player import Player
from lib.snake import Snake
from lib.snake import Table
from sys import exit

pygame.init()

snake = Snake()
table = Table()
x = 0
y = 0
table.insert_at(x, y, 1)
print(table.table)
dt = 0.1
px_of_square = 306
keep_game = True
last_key_pressed = pygame.K_DOWN

clock = pygame.time.Clock()
last_time_moved = 0
snake_speed = 700
snake_head_img = pygame.image.load('lib/snake_head.jpeg')
snake_head_img = pygame.transform.scale(snake_head_img, (snake_head_img.get_width() * 1/10,
                                        snake_head_img.get_height() * 1/10))


screen = pygame.display.set_mode((px_of_square,px_of_square))
pygame.display.set_caption('Snake Game')

while keep_game:

    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    screen.fill((0,0,0))
    screen.blit(snake_head_img, (x,y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    last_key_pressed = Player.get_movement(last_key_pressed ,keys)
    snake.update_direction(last_key_pressed)
    if current_time - last_time_moved > snake_speed:
        last_time_moved = current_time
        snake.move(table)
        x = table.get_snake_position()[0][0] * 34
        y = table.get_snake_position()[0][1] * 34
    print(snake.direction)

    pygame.display.flip()
    clock.tick(60)