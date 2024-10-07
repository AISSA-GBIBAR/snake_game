from settings import *
from snak import Snake
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
    def draw_bg(self):
        self.display_surface.fill(LIGHT_GREEN)
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN , rect )
        
    def run(self):
        while True:
            for event in pygame.event.get(): # ! Polls for all events in the event queue
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.draw_bg()
            self.snake.draw()
            pygame.display.update() # ! Updates the display window in every loop iteration

if __name__ == "__main__":
    main = Main()
    main.run()