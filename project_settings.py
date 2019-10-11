import pygame

pygame.init()  # initialize PyGame
game_font = pygame.font.SysFont('Helvetica', 30)
card_name_font = pygame.font.SysFont('Helvetica', 30)
card_value_font = pygame.font.SysFont('Helvetica', 50)

game_title = 'Dolphin'

clock = pygame.time.Clock()

# game window size
WINDOW_SIZE = (1280, 720)

# Create window to display the game
win = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# Window Title
pygame.display.set_caption(game_title)

# Colors
gray = (100, 100, 100)
light_gray = (200, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
off_white = (233, 233, 233)
black = (0, 0, 0)
orange = (255, 255/2, 0)
purple = (200, 0, 200)

X, Y, Z = 0, 1, 2

gravity = 0.5


class GameSettings(object):

    def __init__(self):
        self.game_font = pygame.font.SysFont('Helvetica', 30)
        self.card_name_font = pygame.font.SysFont('Helvetica', 30)
        self.card_value_font = pygame.font.SysFont('Helvetica', 50)

        self.game_title = 'Dolphin'

        self.clock = pygame.time.Clock()

        # game window size
        self.WINDOW_SIZE = (720, 480)

        self.win = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)
        # Window Title
        pygame.display.set_caption(game_title)

        # Colors
        self.gray = (100, 100, 100)
        self.light_gray = (200, 200, 200)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.off_white = (233, 233, 233)
        self.black = (0, 0, 0)
        self.orange = (255, 255 / 2, 255 / 2)

        X, Y, Z = 0, 1, 2

        gravity = 0.5