from pygame import Surface

from constants import ScreenBounds
from unit import SnakeUnit
from uses_screen import UsesScreen

class Snake(UsesScreen):
    _units: list[SnakeUnit] = []

    def __init__(self, screen: Surface):
        super().__init__(screen)

    def add_unit(self, unit: SnakeUnit):
        self._units.append(unit)

    def draw_self(self):
        for unit in self._units:
            unit.draw_self()

    @property
    def units(self):
        return self._units
    