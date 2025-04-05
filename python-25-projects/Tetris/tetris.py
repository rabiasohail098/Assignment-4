import pygame
import random

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I - Cyan
    (0, 0, 255),    # J - Blue
    (255, 165, 0),  # L - Orange
    (255, 255, 0),  # O - Yellow
    (0, 255, 0),    # S - Green
    (128, 0, 128),  # T - Purple
    (255, 0, 0)     # Z - Red
]

# Game constants
CELL_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
GAME_AREA_LEFT = CELL_SIZE

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    
    [[1, 0, 0],
     [1, 1, 1]],     # J
     
    [[0, 0, 1],
     [1, 1, 1]],     # L
     
    [[1, 1],
     [1, 1]],        # O
     
    [[0, 1, 1],
     [1, 1, 0]],     # S
     
    [[0, 1, 0],
     [1, 1, 1]],     # T
     
    [[1, 1, 0],
     [0, 1, 1]]      # Z
]

class Tetrimino:
    def __init__(self):
        self.shape_idx = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[self.shape_idx]
        self.color = COLORS[self.shape_idx]
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0
        
    def rotate(self):
        # Transpose and reverse each row to rotate 90 degrees clockwise
        rows = len(self.shape)
        cols = len(self.shape[0])
        rotated = [[0 for _ in range(rows)] for _ in range(cols)]
        
        for r in range(rows):
            for c in range(cols):
                rotated[c][rows - 1 - r] = self.shape[r][c]
                
        return rotated
    
    def draw(self, screen):
        for r in range(len(self.shape)):
            for c in range(len(self.shape[0])):
                if self.shape[r][c]:
                    pygame.draw.rect(screen, self.color, 
                                   (GAME_AREA_LEFT + (self.x + c) * CELL_SIZE, 
                                    (self.y + r) * CELL_SIZE, 
                                    CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, WHITE, 
                                   (GAME_AREA_LEFT + (self.x + c) * CELL_SIZE, 
                                    (self.y + r) * CELL_SIZE, 
                                    CELL_SIZE, CELL_SIZE), 1)

class TetrisGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetrimino()
        self.next_piece = Tetrimino()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.fall_speed = 0.5  # seconds
        self.fall_time = 0
        
    def draw_grid(self):
        # Draw game area border
        pygame.draw.rect(self.screen, WHITE, 
                        (GAME_AREA_LEFT - 2, 0, 
                         GRID_WIDTH * CELL_SIZE + 4, 
                         GRID_HEIGHT * CELL_SIZE + 4), 2)
        
        # Draw grid lines
        for x in range(GRID_WIDTH + 1):
            pygame.draw.line(self.screen, GRAY, 
                            (GAME_AREA_LEFT + x * CELL_SIZE, 0),
                            (GAME_AREA_LEFT + x * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
        
        for y in range(GRID_HEIGHT + 1):
            pygame.draw.line(self.screen, GRAY, 
                            (GAME_AREA_LEFT, y * CELL_SIZE),
                            (GAME_AREA_LEFT + GRID_WIDTH * CELL_SIZE, y * CELL_SIZE))
        
        # Draw next piece preview
        font = pygame.font.SysFont('comicsans', 20)
        label = font.render("Next:", 1, WHITE)
        self.screen.blit(label, (GAME_AREA_LEFT + GRID_WIDTH * CELL_SIZE + 20, 10))
        
        next_x = GAME_AREA_LEFT + GRID_WIDTH * CELL_SIZE + 30
        next_y = 40
        
        for r in range(len(self.next_piece.shape)):
            for c in range(len(self.next_piece.shape[0])):
                if self.next_piece.shape[r][c]:
                    pygame.draw.rect(self.screen, self.next_piece.color,
                                   (next_x + c * CELL_SIZE, 
                                    next_y + r * CELL_SIZE, 
                                    CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(self.screen, WHITE,
                                   (next_x + c * CELL_SIZE, 
                                    next_y + r * CELL_SIZE, 
                                    CELL_SIZE, CELL_SIZE), 1)
        
        # Draw score
        score_label = font.render(f"Score: {self.score}", 1, WHITE)
        self.screen.blit(score_label, (GAME_AREA_LEFT + GRID_WIDTH * CELL_SIZE + 20, 120))
        
        # Draw level
        level_label = font.render(f"Level: {self.level}", 1, WHITE)
        self.screen.blit(level_label, (GAME_AREA_LEFT + GRID_WIDTH * CELL_SIZE + 20, 150))
    
    def draw_board(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, COLORS[self.grid[y][x] - 1],
                                    (GAME_AREA_LEFT + x * CELL_SIZE, 
                                     y * CELL_SIZE, 
                                     CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(self.screen, WHITE,
                                    (GAME_AREA_LEFT + x * CELL_SIZE, 
                                     y * CELL_SIZE, 
                                     CELL_SIZE, CELL_SIZE), 1)
    
    def valid_position(self, shape, x, y):
        for r in range(len(shape)):
            for c in range(len(shape[0])):
                if shape[r][c]:
                    if (x + c < 0 or x + c >= GRID_WIDTH or 
                        y + r >= GRID_HEIGHT or 
                        (y + r >= 0 and self.grid[y + r][x + c])):
                        return False
        return True
    
    def lock_piece(self):
        for r in range(len(self.current_piece.shape)):
            for c in range(len(self.current_piece.shape[0])):
                if self.current_piece.shape[r][c]:
                    self.grid[self.current_piece.y + r][self.current_piece.x + c] = self.current_piece.shape_idx + 1
        
        # Check for completed lines
        self.clear_lines()
        
        # Get next piece
        self.current_piece = self.next_piece
        self.next_piece = Tetrimino()
        
        # Check if game over
        if not self.valid_position(self.current_piece.shape, self.current_piece.x, self.current_piece.y):
            self.game_over = True
    
    def clear_lines(self):
        lines_cleared = 0
        for r in range(GRID_HEIGHT):
            if all(self.grid[r]):
                lines_cleared += 1
                # Move all rows above down
                for y in range(r, 0, -1):
                    self.grid[y] = self.grid[y-1][:]
                self.grid[0] = [0] * GRID_WIDTH
        
        # Update score
        if lines_cleared == 1:
            self.score += 100 * self.level
        elif lines_cleared == 2:
            self.score += 300 * self.level
        elif lines_cleared == 3:
            self.score += 500 * self.level
        elif lines_cleared == 4:
            self.score += 800 * self.level
        
        # Update level every 10 lines
        self.level = 1 + self.score // 2000
        self.fall_speed = max(0.05, 0.5 - (self.level - 1) * 0.05)
    
    def run(self):
        last_time = pygame.time.get_ticks()
        
        while not self.game_over:
            current_time = pygame.time.get_ticks()
            delta_time = (current_time - last_time) / 1000.0
            last_time = current_time
            
            self.fall_time += delta_time
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    pygame.quit()
                    return
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.valid_position(self.current_piece.shape, 
                                              self.current_piece.x - 1, 
                                              self.current_piece.y):
                            self.current_piece.x -= 1
                    
                    elif event.key == pygame.K_RIGHT:
                        if self.valid_position(self.current_piece.shape, 
                                              self.current_piece.x + 1, 
                                              self.current_piece.y):
                            self.current_piece.x += 1
                    
                    elif event.key == pygame.K_DOWN:
                        if self.valid_position(self.current_piece.shape, 
                                              self.current_piece.x, 
                                              self.current_piece.y + 1):
                            self.current_piece.y += 1
                    
                    elif event.key == pygame.K_UP:
                        rotated = self.current_piece.rotate()
                        if self.valid_position(rotated, 
                                            self.current_piece.x, 
                                            self.current_piece.y):
                            self.current_piece.shape = rotated
                    
                    elif event.key == pygame.K_SPACE:
                        # Hard drop
                        while self.valid_position(self.current_piece.shape,
                                                self.current_piece.x,
                                                self.current_piece.y + 1):
                            self.current_piece.y += 1
                        self.lock_piece()
                        self.fall_time = 0
            
            # Automatic falling
            if self.fall_time >= self.fall_speed:
                if self.valid_position(self.current_piece.shape, 
                                      self.current_piece.x, 
                                      self.current_piece.y + 1):
                    self.current_piece.y += 1
                else:
                    self.lock_piece()
                self.fall_time = 0
            
            # Drawing
            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_board()
            self.current_piece.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)
        
        # Game over screen
        font = pygame.font.SysFont('comicsans', 40)
        label = font.render("GAME OVER!", 1, WHITE)
        self.screen.blit(label, (SCREEN_WIDTH//2 - label.get_width()//2, 
                               SCREEN_HEIGHT//2 - label.get_height()//2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()