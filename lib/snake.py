import pygame
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
    
    def get_snake_position(self):
        positions = []
        for i in range(9):
            for k in range(9):
                if self.table[i][k] == 1:
                    positions.append([i,k])
        return positions






class Snake:
    def __init__(self):
        self.head = 1
        self.direction = [0,1]
        pass

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
        positions = table.get_snake_position()
        print(positions)
        row = positions[0][0]
        col = positions[0][1]
        if self.direction == [0,1]:
            table.insert_at(row, col + 1, 1)
            table.delete_at(row, col)
        if self.direction == [0,-1]:
            table.insert_at(row, col - 1, 1)
            table.delete_at(row, col)
        if self.direction == [1,0]:
            table.insert_at(row + 1, col, 1)
            table.delete_at(row, col)
        if self.direction == [-1,0]:
            table.insert_at(row - 1, col, 1)
            table.delete_at(row, col)

            
