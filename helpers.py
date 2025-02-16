from pygame import K_w, K_a, K_s, K_d, Rect

from constants import Directions, SPEED


# TODO: Collision detection for when snake hits itself 🪦
def is_snake_hitting_bound(snake_units: list[Rect], borders: list[Rect]) -> bool:
    for border in borders:
        for unit in snake_units:
            if unit.colliderect(border):
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
