import random
from pygame import K_w, K_a, K_s, K_d

from constants import Directions, SPEED, ScreenBounds, SNAKE_UNIT_WIDTH, APPLE_RADIUS
from game_screen import GameScreen
from snake import Snake
from unit import SnakeUnit


# TODO: Collision detection for when snake hits itself 🪦
def is_snake_hitting_bound(game_screen: GameScreen, snake: Snake) -> bool:
    borders = list(game_screen.border.values())
    units = snake.units

    for border in borders:
        for unit in units:
            if unit.rect.colliderect(border):
                return True

    return False


def calculate_next_position(direction_moving: Directions) -> tuple[int, int]:
    if direction_moving == Directions.RIGHT:
        return [SPEED, 0]
    elif direction_moving == Directions.LEFT:
        return [SPEED * -1, 0]
    elif direction_moving == Directions.DOWN:
        return [0, SPEED]
    elif direction_moving == Directions.UP:
        return [0, SPEED * -1]


def calculate_next_direction(key: int, current_direction: str) -> str:
    if key == K_w:
        return Directions.UP
    elif key == K_a:
        return Directions.LEFT
    elif key == K_s:
        return Directions.DOWN
    elif key == K_d:
        return Directions.RIGHT
    else:
        return current_direction


def can_move_in_direction(
    current_direction: Directions, next_direction: Directions
) -> bool:
    horizontal = [Directions.LEFT, Directions.RIGHT]
    vertical = [Directions.UP, Directions.DOWN]

    if current_direction in horizontal and next_direction in horizontal:
        return False
    elif current_direction in vertical and next_direction in vertical:
        return False

    return True


import random
from constants import SNAKE_UNIT_WIDTH, SCREEN_BORDER_WIDTH, APPLE_RADIUS
from unit import SnakeUnit


def next_apple_position(
    screen_bounds: ScreenBounds, units: list[SnakeUnit]
) -> tuple[int, int]:
    padding = 10
    x_min = screen_bounds.LEFT_PLAYABLE + padding
    x_max = screen_bounds.RIGHT_PLAYABLE - padding - SNAKE_UNIT_WIDTH
    y_min = screen_bounds.TOP_PLAYABLE + padding
    y_max = screen_bounds.BOTTOM_PLAYABLE - padding - SNAKE_UNIT_WIDTH
    x_range = range(x_min, x_max + 1, SNAKE_UNIT_WIDTH)
    y_range = range(y_min, y_max + 1, SNAKE_UNIT_WIDTH)
    occupied_positions = {unit.coordinates for unit in units}

    while True:
        x = random.choice(x_range)
        y = random.choice(y_range)

        if (x, y) not in occupied_positions:
            return x, y
