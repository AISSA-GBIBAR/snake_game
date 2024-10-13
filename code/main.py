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
        self.game_active = False
        
        # audio
        self.cruch_sound = pygame.mixer.Sound(join('audio', 'crunch.wav'))
        self.bg_music = pygame.mixer.Sound(join('audio', "Arcade.ogg"))
        self.bg_music.set_volume(0.3)
        self.bg_music.play(-1)
        
    def draw_bg(self):
        self.display_surface.fill(LIGHT_GREEN)
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN , rect )
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: 
            self.snake.direction = pygame.Vector2(1, 0) if self.snake.direction.x != -1 else self.snake.direction
        if keys[pygame.K_LEFT]: 
            self.snake.direction = pygame.Vector2(-1, 0) if self.snake.direction.x != 1 else self.snake.direction
        if keys[pygame.K_UP]: 
            self.snake.direction = pygame.Vector2(0, -1) if self.snake.direction.y != 1 else self.snake.direction
        if keys[pygame.K_DOWN]: 
            self.snake.direction = pygame.Vector2(0, 1) if self.snake.direction.y != -1 else self.snake.direction
    
    def collision(self):
        # apple
        if self.snake.body[0] ==  self.apple.pos:
            self.snake.has_eaten = True
            self.apple.set_pos()
            self.cruch_sound.play()
        
        # game over
        if self.snake.body[0] in self.snake.body[1:] or \
            not 0 <= self.snake.body[0].x < COLS or \
            not 0 <= self.snake.body[0].y < ROWS:
            
            self.snake.reset()
            self.game_active = False
    
    def draw_shadow(self):
        shadow_surf = pygame.Surface(self.display_surface.get_size())
        shadow_surf.fill((0, 255, 0))
        shadow_surf.set_colorkey((0, 255, 0))
        
        # surf
        shadow_surf.blit(self.apple.scaled_surf ,self.apple.scaled_rect.topleft + SHADOW_SIZE)
        for surf, rect in self.snake.draw_data:
            shadow_surf.blit(surf, rect.topleft + SHADOW_SIZE)
        mask = pygame.mask.from_surface(shadow_surf)
        mask.invert()
        shadow_surf = mask.to_surface()
        shadow_surf.set_colorkey((255, 255, 255))
        shadow_surf.set_alpha(SHADOW_OPACITY)
        
        self.display_surface.blit(shadow_surf, (0,0))
    def run(self):
        while True:
            for event in pygame.event.get(): # ! Polls for all events in the event queue
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.update_event and self.game_active:
                    # Update the snake body
                    self.snake.update()
                
                if event.type == pygame.KEYDOWN and not self.game_active:
                    self.game_active = True
            
            #moving snake 
            self.input()
            self.collision()
            
            # drwaing         
            self.draw_bg()
            self.draw_shadow()
            self.snake.draw()
            self.apple.draw()
            pygame.display.update() # ! Updates the display window in every loop iteration

if __name__ == "__main__":
    main = Main()
    main.run()