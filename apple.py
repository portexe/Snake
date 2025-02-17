from pygame import Surface, draw, Rect

from uses_screen import UsesScreen

from constants import RED, APPLE_RADIUS, GREEN

class Apple(UsesScreen):
    def __init__(self, screen: Surface, initial_x: int, initial_y: int):
        super().__init__(screen)
        self.x = initial_x
        self.y = initial_y
        self.draw_self()
        
    def draw_self(self):
        draw.circle(self.screen, RED, (self.x, self.y), APPLE_RADIUS)
        draw.circle(self.screen, GREEN, (self.x + 10, self.y - 15), 5)
        self.rect = Rect(self.x - APPLE_RADIUS, self.y - APPLE_RADIUS, APPLE_RADIUS * 2, APPLE_RADIUS * 2)

    def update_location(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def apple_rect(self):
        return self.rect
