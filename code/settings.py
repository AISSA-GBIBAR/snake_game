import pygame
from sys import exit
from os.path import join

CELL_SIZE = 65
ROWS = 10
COLS = 16
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE


#this color
LIGHT_GREEN = "#aad751"
DARK_GREEN = "#aff25a"

#start pos
START_LENGTH = 3
START_ROW = ROWS // 2
START_COL = START_LENGTH + 2

#shadowS
SHADOW_SIZE = pygame.Vector2(4, 4)
SHADOW_OPACITY = 50