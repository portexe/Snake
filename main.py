import pygame
from math import floor, ceil

from helpers import (
    is_snake_hitting_bound,
    calculate_next_position,
    calculate_next_direction,
    can_move_in_direction,
    next_apple_position,
)
from constants import DIRECTION_KEYS, SNAKE_UNIT_WIDTH, SPEED

from apple import Apple
from game_screen import GameScreen
from snake import Snake
from unit import SnakeUnit

pygame.init()
clock = pygame.time.Clock()
game_screen = GameScreen()
screen = game_screen.screen
screen_border = game_screen.border
screen_bounds = game_screen.screen_bounds

# Game state
game_running = True

initial_x_pos = floor(screen_bounds.RIGHT_PLAYABLE / 2)
initial_y_pos = ceil(screen_bounds.BOTTOM_PLAYABLE / 2)

snake = Snake(screen)

for multiplier in range(1, 4):
    x = initial_x_pos - (multiplier * SNAKE_UNIT_WIDTH)
    y = initial_y_pos
    snake.add_unit(SnakeUnit(screen, x, y, multiplier == 1))


# TODO: Next up: we need to store pivot events.
# 1. These pivot events will need to exist as a queue.
# 2. When the snake turns in any direction we will need to store this event in the queue
# 3. Every unit will need to follow the same pivot path.
# 4. Once every unit has followed the path, it can be removed from the queue.

apple_x, apple_y = next_apple_position(game_screen.screen_bounds, snake.units)
apple = Apple(screen, apple_x, apple_y)

while game_running:
    if is_snake_hitting_bound(game_screen, snake):
        game_running = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN and event.key in DIRECTION_KEYS:
            current_direction = snake.direction_moving
            next_direction = calculate_next_direction(event.key, current_direction)

            if can_move_in_direction(current_direction, next_direction):
                snake.add_pivot(
                    snake.units[0].coordinates[0],
                    snake.units[0].coordinates[1],
                    current_direction,
                )
                snake.update_direction(next_direction)

    x_increment, y_increment = calculate_next_position(snake.direction_moving)

    for unit in snake.units:
        x, y = unit.coordinates
        if unit.needs_to_pivot:
            x_increment_toward_pivot, y_increment_toward_pivot = (
                calculate_next_position(unit.direction_to_pivot)
            )
            unit.move_to(x + x_increment_toward_pivot, y + y_increment_toward_pivot)
            if (
                abs(unit.coordinates[0] - unit.pivot[0]) < SPEED
                and abs(unit.coordinates[1] - unit.pivot[1]) < SPEED
            ):
                unit.move_to(*unit.pivot)
                unit.set_pivot_reached()
        else:
            unit.move_to(x + x_increment, y + y_increment)

    if snake.detect_apple_collision(apple.apple_rect):
        new_apple_x, new_apple_y = next_apple_position(game_screen.screen_bounds, snake.units)
        apple.update_location(new_apple_x, new_apple_y)
        snake.add_unit(snake.generate_new_unit())

    screen.fill("black")

    apple.draw_self()
    game_screen.draw_self()
    snake.draw_self()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
