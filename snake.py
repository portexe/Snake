from pygame import Surface, Rect

from constants import Directions, SNAKE_UNIT_WIDTH
from unit import SnakeUnit
from uses_screen import UsesScreen


class Snake(UsesScreen):
    _units: list[SnakeUnit] = []
    _direction_moving = Directions.RIGHT

    def __init__(self, screen: Surface):
        super().__init__(screen)

    def add_unit(self, unit: SnakeUnit):
        self._units.append(unit)

    def draw_self(self):
        for unit in self._units:
            unit.draw_self()

    def update_direction(self, direction: Directions):
        self._direction_moving = direction

    def add_pivot(self, x: int, y: int, direction: Directions):
        for unit in self.units[1:]:
            unit.add_pivot(x, y, direction)

    def detect_apple_collision(self, apple_rect: Rect) -> bool:
        for unit in self.units:
            if unit.rect.colliderect(apple_rect):
                return True
        return False

    # TODO: Needs to work with pivots
    def generate_new_unit(self) -> SnakeUnit:
        closest_unit_x, closest_unit_y = self._units[-1].coordinates
        direction = self._direction_moving

        if direction == Directions.RIGHT:
            new_x, new_y = closest_unit_x - SNAKE_UNIT_WIDTH, closest_unit_y
        elif direction == Directions.LEFT:
            new_x, new_y = closest_unit_x + SNAKE_UNIT_WIDTH, closest_unit_y
        elif direction == Directions.DOWN:
            new_x, new_y = closest_unit_x, closest_unit_y - SNAKE_UNIT_WIDTH
        elif direction == Directions.UP:
            new_x, new_y = closest_unit_x, closest_unit_y + SNAKE_UNIT_WIDTH
        else:
            new_x, new_y = closest_unit_x, closest_unit_y

        return SnakeUnit(self.screen, new_x, new_y, False)

    @property
    def units(self):
        return self._units

    @property
    def direction_moving(self):
        return self._direction_moving
