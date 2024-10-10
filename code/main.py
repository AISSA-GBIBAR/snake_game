from settings import *
from snak import Snake
from apple import Apple
class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game By Aissa Gbibar")
        
        #game object 
        # ? create a rectangle object in Pygame
        self.bg_rects = [
            pygame.Rect(
                (col + int(row % 2 == 0)) * CELL_SIZE,  # X-coordinate
                row*CELL_SIZE,# Y-coordinate
                CELL_SIZE, # Width of the rectangle
                CELL_SIZE) # Height of the rectangle    
                for col in range(0,COLS, 2) # Iterates over columns, skipping every other column (step of 2)
                for row in range(ROWS)] # Iterates over rows
        self.snake = Snake()
        self.apple = Apple(self.snake)
        
        # timer 
        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 200)
        
    def draw_bg(self):
        self.display_surface.fill(LIGHT_GREEN)
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN , rect )
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.snake.direction = pygame.Vector2(1, 0)
        if keys[pygame.K_LEFT]: self.snake.direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_UP]: self.snake.direction = pygame.Vector2(0, -1)
        if keys[pygame.K_DOWN]: self.snake.direction = pygame.Vector2(0, 1)
    
    def run(self):
        while True:
            for event in pygame.event.get(): # ! Polls for all events in the event queue
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.update_event:
                    # Update the snake body
                    self.snake.update()
            
            #moving snake body
            self.input()
            
            # drwaing         
            self.draw_bg()
            self.snake.draw()
            self.apple.draw()
            pygame.display.update() # ! Updates the display window in every loop iteration

if __name__ == "__main__":
    main = Main()
    main.run()