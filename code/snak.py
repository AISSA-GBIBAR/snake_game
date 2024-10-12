from settings import *

class Snake:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.body = [pygame.Vector2(START_COL - col, START_ROW) for col in range(START_LENGTH)]
        self.direction = pygame.Vector2(1, 0)
        
        self.has_eaten = False
    def update(self):
        if not self.has_eaten:
            body_copy = self.body[:-1]   
        else:
            body_copy = self.body[:]   
            self.has_eaten = False
        # 1 . get the head and move the head direction
        new_head = self.body[0] + self.direction
        # 2 . insert the new head at index 0
        body_copy.insert(0, new_head)  
        # update the original body
        self.body = body_copy[:]
        
    def draw(self):
        for point in self.body:
            rect = (point.x * CELL_SIZE, point.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.display_surface, "red" ,rect)
    
    def reset(self):
        self.body = [pygame.Vector2(START_COL - col, START_ROW) for col in range(START_LENGTH)]
        self.direction = pygame.Vector2(1, 0)