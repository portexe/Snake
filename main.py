import pygame
from pygame import Rect
from math import floor, ceil

from helpers import (
    is_snake_hitting_bound,
    calculate_next_position,
    calculate_next_direction,
)
from constants import (
    ScreenBounds,
    Directions,
    GREEN,
    SNAKE_UNIT_WIDTH,
    DARK_GREEN,
    SCREEN_BORDER_WIDTH,
)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))

# Game state
game_running = True
direction_moving = Directions.RIGHT
screen_bounds = ScreenBounds(screen)
x_pos = floor(screen_bounds.RIGHT_PLAYABLE / 2)
y_pos = ceil(screen_bounds.BOTTOM_PLAYABLE / 2)
borders: list[Rect] = []
unit_rects: list[Rect] = []
total_snake_units = 3

# TODO: Next up: we need to store pivot events.
# 1. These pivot events will need to exist as a queue.
# 2. When the snake turns in any direction we will need to store this event in the queue
# 3. Every unit will need to follow the same pivot path.
# 4. Once every unit has followed the path, it can be removed from the queue.


def _draw_border() -> list[Rect]:
    screen_border_left = Rect(
        screen_bounds.LEFT, screen_bounds.TOP, SCREEN_BORDER_WIDTH, screen_bounds.BOTTOM
    )
    screen_border_top = Rect(
        screen_bounds.LEFT, screen_bounds.TOP, screen_bounds.RIGHT, SCREEN_BORDER_WIDTH
    )
    screen_border_right = Rect(
        screen_bounds.RIGHT - SCREEN_BORDER_WIDTH,
        screen_bounds.TOP,
        SCREEN_BORDER_WIDTH,
        screen_bounds.BOTTOM,
    )
    screen_border_bottom = Rect(
        screen_bounds.LEFT,
        screen_bounds.BOTTOM - SCREEN_BORDER_WIDTH,
        screen_bounds.RIGHT,
        SCREEN_BORDER_WIDTH,
    )

    pygame.draw.rect(screen, DARK_GREEN, screen_border_left)
    pygame.draw.rect(screen, DARK_GREEN, screen_border_top)
    pygame.draw.rect(screen, DARK_GREEN, screen_border_right)
    pygame.draw.rect(screen, DARK_GREEN, screen_border_bottom)

    return [
        screen_border_left,
        screen_border_top,
        screen_border_right,
        screen_border_bottom,
    ]


def _draw_snake() -> list[Rect]:
    rects = []

    for snake_unit in range(1, total_snake_units + 1):
        x_multiplier = snake_unit * SNAKE_UNIT_WIDTH
        # y_multiplier = ???

        outer_rect = Rect(
            (x_pos + x_multiplier, y_pos, SNAKE_UNIT_WIDTH, SNAKE_UNIT_WIDTH)
        )
        inner_rect = Rect(
            (
                x_pos + x_multiplier + 5,
                y_pos + 5,
                SNAKE_UNIT_WIDTH - 10,
                SNAKE_UNIT_WIDTH - 10,
            )
        )

        pygame.draw.rect(screen, DARK_GREEN, outer_rect)
        pygame.draw.rect(screen, GREEN, inner_rect)

        rects.append(outer_rect)

    return rects


while game_running:
    if is_snake_hitting_bound(unit_rects, borders):
        game_running = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            direction_moving = calculate_next_direction(event.key, direction_moving)

    x_increment, y_increment = calculate_next_position(direction_moving)
    x_pos += x_increment
    y_pos += y_increment

    screen.fill("black")

    borders = _draw_border()
    unit_rects = _draw_snake()
    total_snake_units = len(unit_rects)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
