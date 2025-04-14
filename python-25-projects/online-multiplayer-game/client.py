import pygame
from network import Network

pygame.init()

width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Multiplayer Game")

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 50
        self.height = 50
        self.vel = 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.x -= self.vel
        if keys[pygame.K_RIGHT]: self.x += self.vel
        if keys[pygame.K_UP]: self.y -= self.vel
        if keys[pygame.K_DOWN]: self.y += self.vel

def read_pos(string):
    x, y = map(int, string.split(","))
    return x, y

def make_pos(tup):
    return f"{tup[0]},{tup[1]}"

def redraw_window(win, player, opponent):
    win.fill((255, 255, 255))
    player.draw(win)
    opponent.draw(win)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    net = Network()
    start_pos = read_pos(net.pos)

    player = Player(start_pos[0], start_pos[1], (0, 255, 0))  # You
    opponent = Player(0, 0, (255, 0, 0))  # Other

    while run:
        clock.tick(60)
        try:
            net_data = net.send(make_pos((player.x, player.y)))
            opp_x, opp_y = read_pos(net_data)
            opponent.x = opp_x
            opponent.y = opp_y
        except:
            print("Connection lost.")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.move()
        redraw_window(win, player, opponent)

    pygame.quit()

main()
