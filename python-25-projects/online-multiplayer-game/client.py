# import pygame
# from network import Network  
# # Initialize pygame
# pygame.init()

# # Screen dimensions
# width = 800
# height = 600
# win = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Client")

# clientNumber = 0

# class Player:
#     def __init__(self, x, y, width, height, color):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.color = color
#         self.rect = (x, y, width, height)
#         self.val = 3
     
#     def draw(self, window):  # Fixed method name from 'raw' to 'draw'
#         pygame.draw.rect(window, self.color, self.rect)
    
#     def move(self):
#         keys = pygame.key.get_pressed()  # Fixed from pygame.keys to pygame.key
        
#         if keys[pygame.K_LEFT]:
#             self.x -= self.val
#         if keys[pygame.K_RIGHT]:
#             self.x += self.val  
#         if keys[pygame.K_UP]:
#             self.y -= self.val
#         if keys[pygame.K_DOWN]:
#             self.y += self.val
#         self.update()
#     def update(self):
#         self.rect = (self.x, self.y, self.width, self.height)
# def read_pos(str):
#     str = str.split(",")
#     return (int(str[0]), int(str[1]))

# def make_pos(top):
#     return str(top[0]) + "," + str(top[1])


    
             
# def redraw_window(window, player,player2):  # Added window parameter
#     window.fill((255, 255, 255))  # Fixed color value (225 to 255)
#     player.draw(window)
#     player2.draw(window)  
#     pygame.display.update()
    
# def main():
#     run = True
#     n = Network()
#     startpos = read_pos(n.getPos())
#     p = Player(startpos[0],startpos[1], 100, 100, (0, 255, 0))
#     p2 = Player(0, 0, 100, 100, (255, 0, 0))
#     clock = pygame.time.Clock()
    
#     while run:
#         clock.tick(60)
        
#         p2_pos = read_pos(n.send(make_pos((p.x, p.y))))
#         p2,x = p2_pos[0]
#         p2.y = p2_pos[1]
#         p2.update()
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()
        
#         p.move()       
#         redraw_window(win, p,p2)  # Fixed parameter order
    
#     pygame.quit()  # Moved quit outside the while loop
 
    
# main()
import pygame
from network import Network  

# Initialize pygame
pygame.init()

# Screen dimensions
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 3
     
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.val
        if keys[pygame.K_RIGHT]:
            self.x += self.val  
        if keys[pygame.K_UP]:
            self.y -= self.val
        if keys[pygame.K_DOWN]:
            self.y += self.val
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(data):
    try:
        x, y = map(int, data.split(","))
        return x, y
    except:
        return 0, 0  # fallback

def make_pos(pos):
    return f"{pos[0]},{pos[1]}"

def redraw_window(window, player, player2):
    window.fill((255, 255, 255))  
    player.draw(window)
    player2.draw(window)  
    pygame.display.update()

def main():
    run = True
    n = Network()
    pos = n.getPos()
    
    if pos is None:
        print("Could not connect to server")
        return

    start_x, start_y = read_pos(pos)
    p = Player(start_x, start_y, 100, 100, (0, 255, 0))  # This client's player
    p2 = Player(0, 0, 100, 100, (255, 0, 0))             # Opponent player
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)

        try:
            p2_pos = read_pos(n.send(make_pos((p.x, p.y))))
            p2.x = p2_pos[0]
            p2.y = p2_pos[1]
            p2.update()
        except:
            print("Connection lost")
            run = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        p.move()
        redraw_window(win, p, p2)

    pygame.quit()

main()

