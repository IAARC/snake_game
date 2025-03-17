import pygame
import random
class Table:
    def __init__(self):
        self.table = [[0 for _ in range(9)] for _ in range(9)]
        self.collision = False

    def insert_at(self, row, col, element):
        row = int(row)
        col = int(col)
        if self.valid_position(col,row):
            self.table[row][col] = element
        else:
            self.collision = True
    
    def delete_at(self, row, col):
        self.table[row][col] = 0
 

    def valid_position(self, row, col):
        return 0 <= int(col) <= 8 and 0 <= int(row) <= 8
    
    def get_element_position(self, element):
        positions = []
        for i in range(9):
            for k in range(9):
                if self.table[i][k] == element:
                    positions.append([i,k])
        return positions
    
    def random_position(self):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        while self.table[x][y] != 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8) 
        return x, y

    def insert_apple(self):
        x, y = self.random_position()
        self.insert_at(x , y , 2)

    def clear(self):
        apple_position = self.get_element_position(2)
        if apple_position:
            x , y = apple_position[0]
            self.table = [[0 for _ in range(9)] for _ in range(9)]
            self.table[x][y] = 2
        else:
            self.table = [[0 for _ in range(9)] for _ in range(9)]

    
    def update_table(self, positions):
        self.clear()

        for key in positions:
            if key == 'head':
                self.insert_at(*positions[key], 1)
            else:
                for position in positions['body']:
                    print(positions)
                    self.insert_at(*position, 3)





class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('lib/snake_head.png')
        self.rect = self.image.get_rect()
        self.direction = [0,1]
        self.positions = { 'head': [0,0],
                            'body': []
        }

    def update_direction(self, key_pressed):

        if key_pressed == pygame.K_UP:
            self.direction[1] = -1
            self.direction[0] = 0
        elif key_pressed == pygame.K_DOWN:
            self.direction[1] = 1
            self.direction[0] = 0
        elif key_pressed == pygame.K_LEFT:
            self.direction[1] = 0
            self.direction[0] = -1
        elif key_pressed == pygame.K_RIGHT:
            self.direction[1] = 0
            self.direction[0] = 1

    def move(self, table):
        old_head_position_x, old_head_position_y = self.positions['head'][0], self.positions['head'][1]
        old_body_position_x, old_body_position_y = old_head_position_x, old_head_position_y
        if self.direction == [0,1]:
            self.positions['head'] = [old_head_position_x, old_head_position_y + 1]
        if self.direction == [0,-1]:
            self.positions['head'] = [old_head_position_x, old_head_position_y - 1]
        if self.direction == [1,0]:
            self.positions['head'] = [old_head_position_x + 1, old_head_position_y]
        if self.direction == [-1,0]:
            self.positions['head'] = [old_head_position_x - 1, old_head_position_y]

        for i in range(len(self.positions['body'])):
            temp_x, temp_y = self.positions['body'][i]
            self.positions['body'][i] = [old_body_position_x, old_body_position_y]
            old_body_position_x, old_body_position_y = temp_x, temp_y
        
        table.update_table(self.positions)


    def node(self, table):
        if self.positions['body'] == []:
            x, y = [x + y for x, y in zip(self.direction, self.positions['head'])]
            self.positions['body'].append([x,y])
        else:
            x, y = [x + y for x, y in zip(self.direction, self.positions['body'][-1])]
            self.positions['body'].append([x,y])

class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('lib/apple.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.position = [[x/34, y/34]]

