from pygame import K_w, K_a, K_s, K_d, Surface

DIRECTION_KEYS = [K_w, K_a, K_s, K_d]

# Game physics and measurements
SNAKE_UNIT_WIDTH = 35
SPEED = 3
SCREEN_BORDER_WIDTH = 10
APPLE_RADIUS = 17

# Colors
GREEN = "green"
DARK_GREEN = (0, 150, 0)
RED = (255, 0, 0)


# Enums
class Directions:
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"


class ScreenBounds:
    def __init__(self, screen: Surface):
        self.TOP = screen.get_rect().top
        self.LEFT = screen.get_rect().left
        self.RIGHT = screen.get_rect().right
        self.BOTTOM = screen.get_rect().bottom
        self.TOP_PLAYABLE = screen.get_rect().top + SCREEN_BORDER_WIDTH
        self.LEFT_PLAYABLE = screen.get_rect().left + SCREEN_BORDER_WIDTH
        self.RIGHT_PLAYABLE = screen.get_rect().right - SCREEN_BORDER_WIDTH
        self.BOTTOM_PLAYABLE = screen.get_rect().bottom - SCREEN_BORDER_WIDTH
