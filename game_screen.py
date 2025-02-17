from pygame import display, Surface, Rect, draw

from constants import DARK_GREEN, SCREEN_BORDER_WIDTH, ScreenBounds


class GameScreen:
    def __init__(self):
        self._screen = display.set_mode((1280, 720))
        self._screen_bounds = ScreenBounds(self._screen)
        self.create_border()

    def create_border(self):
        self._screen_border_left = Rect(
            self._screen_bounds.LEFT,
            self._screen_bounds.TOP,
            SCREEN_BORDER_WIDTH,
            self._screen_bounds.BOTTOM,
        )
        self._screen_border_top = Rect(
            self._screen_bounds.LEFT,
            self._screen_bounds.TOP,
            self._screen_bounds.RIGHT,
            SCREEN_BORDER_WIDTH,
        )
        self._screen_border_right = Rect(
            self._screen_bounds.RIGHT - SCREEN_BORDER_WIDTH,
            self._screen_bounds.TOP,
            SCREEN_BORDER_WIDTH,
            self._screen_bounds.BOTTOM,
        )
        self._screen_border_bottom = Rect(
            self._screen_bounds.LEFT,
            self._screen_bounds.BOTTOM - SCREEN_BORDER_WIDTH,
            self._screen_bounds.RIGHT,
            SCREEN_BORDER_WIDTH,
        )

    def draw_self(self):
        draw.rect(self._screen, DARK_GREEN, self._screen_border_left)
        draw.rect(self._screen, DARK_GREEN, self._screen_border_top)
        draw.rect(self._screen, DARK_GREEN, self._screen_border_right)
        draw.rect(self._screen, DARK_GREEN, self._screen_border_bottom)

    @property
    def screen(self) -> Surface:
        return self._screen

    @property
    def border(self):
        return {
            "left": self._screen_border_left,
            "top": self._screen_border_top,
            "right": self._screen_border_right,
            "bottom": self._screen_border_bottom,
        }

    @property
    def screen_bounds(self) -> ScreenBounds:
        return self._screen_bounds
