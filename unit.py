from pygame import Surface, Rect, draw

from constants import Directions, SPEED, GREEN, DARK_GREEN, SNAKE_UNIT_WIDTH
from uses_screen import UsesScreen


class SnakeUnit(UsesScreen):
    def __init__(self, screen: Surface, x: int, y: int, is_head: bool):
        super().__init__(screen)
        self._x = x
        self._y = y
        self._is_head = is_head
        self.move_to(self._x, self._y)
        self._pivot: list[tuple[tuple[int, int], Directions]] = []

    def move_to(self, x: int, y: int):
        self._x = x
        self._y = y
        self._rect = Rect((self._x, self._y, SNAKE_UNIT_WIDTH, SNAKE_UNIT_WIDTH))

        self._inner_rect_left = Rect((self._x, self._y, 5, SNAKE_UNIT_WIDTH))

        self._inner_rect_right = Rect(
            (self._x + SNAKE_UNIT_WIDTH - 5, self._y, 5, SNAKE_UNIT_WIDTH)
        )

        self._inner_rect_top = Rect((self._x, self._y, SNAKE_UNIT_WIDTH, 5))

        self._inner_rect_bottom = Rect(
            (self._x, self._y + SNAKE_UNIT_WIDTH - 5, SNAKE_UNIT_WIDTH, 5)
        )

    def draw_self(self):
        draw.rect(self.screen, GREEN, self._rect)
        draw.rect(self.screen, DARK_GREEN, self._inner_rect_left)
        draw.rect(self.screen, DARK_GREEN, self._inner_rect_right)
        draw.rect(self.screen, DARK_GREEN, self._inner_rect_top)
        draw.rect(self.screen, DARK_GREEN, self._inner_rect_bottom)

    def add_pivot(self, x: int, y: int, direction: Directions):
        if self._is_head:
            raise Exception("Should not be calling add_pivot in head")
        self._pivot.append(((x, y), direction))

    def set_pivot_reached(self):
        if self._is_head:
            raise Exception("Should not be calling set_pivot_reached in head")
        self._pivot.pop(0)

    @property
    def coordinates(self):
        return (self._x, self._y)

    @property
    def rect(self):
        return self._rect

    @property
    def pivot(self):
        if self._is_head:
            raise Exception("Should not be calling pivot in head")
        return self._pivot[0][0]

    @property
    def needs_to_pivot(self):
        if self._is_head and len(self._pivot) > 0:
            raise Exception("Head should not have any pivots")
        return len(self._pivot) > 0

    @property
    def direction_to_pivot(self):
        if self._is_head:
            raise Exception("Should not be calling direction_to_pivot in head")
        return self._pivot[0][1]

    @property
    def is_head(self):
        return self._is_head
