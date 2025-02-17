from pygame import Surface, Rect, draw

from constants import GREEN, DARK_GREEN, SNAKE_UNIT_WIDTH
from uses_screen import UsesScreen


class SnakeUnit(UsesScreen):
    def __init__(self, screen: Surface, x: int, y: int):
        super().__init__(screen)
        self._x = x
        self._y = y
        self.move_to(self._x, self._y)

    def move_to(self, x: int, y: int):
        self._x = x
        self._y = y
        self._rect = Rect((self._x, self._y, SNAKE_UNIT_WIDTH, SNAKE_UNIT_WIDTH))
        self.inner_rect = Rect(
            (
                self._x + 5,
                self._y + 5,
                SNAKE_UNIT_WIDTH - 10,
                SNAKE_UNIT_WIDTH - 10,
            )
        )

    def draw_self(self):
        draw.rect(self.screen, DARK_GREEN, self._rect)
        draw.rect(self.screen, GREEN, self.inner_rect)

    @property
    def coordintaes(self):
        return (self._x, self._y)

    @property
    def rect(self):
        return self._rect
