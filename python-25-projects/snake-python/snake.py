# import math
# import random
# import pygame
# import tkinter as tk
# from tkinter import messagebox

# class Cube(object):
#     rows = 0
#     w = 0
#     def __init__(self, start, dir_x=1, dir_y=0, color=(0, 255, 0)):
#         pass
    
    
#     def move(self, dir_x, dir_y):
#         pass
    
    
#     def draw(self, surface, eyes=False):
#          pass
    
# class Snake(object):
#     body = []
#     turns = {}
    
#     def __init__(self, color, pos):
#         self.color = color
#         self.head = Cube(pos)
#         self.body.append(self.head)
#         self.dir_x = 0
#         self.dir_y = 1
       
    
    
#     def move(self):
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
                
#             keys = pygame.key.get_pressed()
            
#             for key in keys:
#                 if keys[pygame.K_LEFT]:
#                     self.dir_x = -1
#                     self.dir_x = 0
#                     self.turns[self.head.pos[:]] = (self.dir_x, self.dir_y)
                    
                    
#                 elif keys[pygame.K_RIGHT]:
#                     self.dir_x = 0
#                     self.dir_x = -1
#                     self.turns[self.head.pos[:]] = (self.dir_x, self.dir_y)
                    
                    
#                 elif keys[pygame.K_UP]:
#                     self.dir_x = 0
#                     self.dir_x = -1
#                     self.turns[self.head.pos[:]] = (self.dir_x, self.dir_y)
                    
                    
#                 elif keys[pygame.K_DOWN]:
#                     self.dir_x = 0
#                     self.dir_x = 1
#                     self.turns[self.head.pos[:]] = (self.dir_x, self.dir_y)
                       
#         for i, c in enumerate(self.body):
#             p = c.pos[:]
#             if p in self.turns:
#                 turn = self.turns[p]
#                 c.move(turn[0], turn[1])
#                 if i == len(self.body) - 1:
#                     self.turns.pop(p)
                  
#             else:
#                 if c.dir_x == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[1])
#                 elif c.dir_x == 1 and c.pos[0] >= c.rows - 1: c.pos = (0, c.pos[1])
#                 elif c.dir_y == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
#                 elif c.dir_y == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
#                 else:
#                     c.move(c.dir_x, c.dir_y)
                    
                    
                    
                    
#         for i, c in enumerate(self.body):
#             c.move(self.turns[c][0], self.turns[c][1])
    
    
#     def reset(self, pos):
#         pass
    
    
#     def add_cube(self):
#         pass 
    

#     def draw(self, surface):
#         for i, c in enumerate(self.body):
#             if i == 0:
#                 c.draw(surface, True)
#             else:
#                 c.draw(surface)
    
    
    
# def draw_grid(surface, rows, width):
#     size_between = width // rows
#     x = 0
#     y = 0
#     for i in range(rows):
#         x += size_between
#         y += size_between
        
#         pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
#         pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


# def redraw_window( surface):
#     surface.fill((0, 0, 0))
#     draw_grid(width, rows, surface)
#     pygame.display.update()


# def random_snack(rows, items):
#     pass


# def message_box(subject, content):
#     pass

# def main():
#     global width,rows
#     width = 800
#     rows = 20
#     win = pygame.display.set_mode((width, width))
#     s = Snake((255, 0, 0), (10, 10))
#     flag = True
    
#     clock = pygame.time.Clock()
    
    
#     while flag:
#         pygame.time.delay(50)
#         clock.tick(10)
#         redraw_window(win, win)
#     pass


# main()
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    rows = 20
    w = 500
    
    def __init__(self, start, dir_x=1, dir_y=0, color=(0, 255, 0)):
        self.pos = start
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.color = color
    
    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0] + dir_x, self.pos[1] + dir_y)
    
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i*dis + centre - radius, j*dis + 8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

class Snake(object):
    body = []
    turns = {}
    
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dir_x = 0
        self.dir_y = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.dir_x = -1
            self.dir_y = 0
            self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
            
        elif keys[pygame.K_RIGHT]:
            self.dir_x = 1
            self.dir_y = 0
            self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
            
        elif keys[pygame.K_UP]:
            self.dir_x = 0
            self.dir_y = -1
            self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
            
        elif keys[pygame.K_DOWN]:
            self.dir_x = 0
            self.dir_y = 1
            self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
               
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dir_x == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[1])
                elif c.dir_x == 1 and c.pos[0] >= c.rows - 1: c.pos = (0, c.pos[1])
                elif c.dir_y == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
                elif c.dir_y == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dir_x, c.dir_y)
    
    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1
    
    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dir_x, tail.dir_y
        
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))
        
        self.body[-1].dir_x = dx
        self.body[-1].dir_y = dy
    
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def draw_grid(surface, rows, width):
    size_between = width // rows
    x = 0
    y = 0
    for _ in range(rows):
        x += size_between
        y += size_between
        
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))

def redraw_window(surface, snake, snack):
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(surface, rows, width)
    pygame.display.update()

def random_snack(rows, snake):
    positions = snake.body
    
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
            
    return (x, y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption('Snake Game')
    
    s = Snake((0, 255, 0), (10, 10))
    snack = Cube(random_snack(rows, s), color=(255, 0, 0))
    flag = True
    
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = Cube(random_snack(rows, s), color=(255, 0, 0))
            
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                print(f'Score: {len(s.body)}')
                message_box('You Lost!', f'Play again...\nScore: {len(s.body)}')
                s.reset((10, 10))
                break
                
        redraw_window(win, s, snack)

main()