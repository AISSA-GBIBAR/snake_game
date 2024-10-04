from settings import *

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game By Aissa Gbibar")
        
        #game object 
        self.bg_rects = [pygame.Rect((col + int(row % 2 == 0)) * CELL_SIZE, row*CELL_SIZE,CELL_SIZE, CELL_SIZE) 
                         for col in range(0,COLS, 2) for row in range(ROWS)]
    
    def draw_bg(self):
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN , rect )
        
    def run(self):
        while True:
            for event in pygame.event.get(): # ! Polls for all events in the event queue
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.display_surface.fill(LIGHT_GREEN)
            self.draw_bg()
            pygame.display.update() # ! Updates the display window in every loop iteration

if __name__ == "__main__":
    main = Main()
    main.run()