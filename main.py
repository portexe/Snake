import pygame
from math import floor, ceil

from helpers import (
    is_snake_hitting_bound,
    calculate_next_position,
    calculate_next_direction,
)
from constants import (
    Directions,
    SNAKE_UNIT_WIDTH,
)

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
direction_moving = Directions.RIGHT

initial_x_pos = floor(screen_bounds.RIGHT_PLAYABLE / 2)
initial_y_pos = ceil(screen_bounds.BOTTOM_PLAYABLE / 2)

snake = Snake(screen)

for multiplier in range(1, 4):
    x = initial_x_pos + (multiplier * SNAKE_UNIT_WIDTH)
    y = initial_y_pos
    snake.add_unit(SnakeUnit(screen, x, y))


# TODO: Next up: we need to store pivot events.
# 1. These pivot events will need to exist as a queue.
# 2. When the snake turns in any direction we will need to store this event in the queue
# 3. Every unit will need to follow the same pivot path.
# 4. Once every unit has followed the path, it can be removed from the queue.


while game_running:
    if is_snake_hitting_bound(game_screen, snake):
        game_running = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            direction_moving = calculate_next_direction(event.key, direction_moving)

    x_increment, y_increment = calculate_next_position(direction_moving)
    for unit in snake.units:
        x, y = unit.coordintaes
        unit.move_to(x + x_increment, y + y_increment)

    screen.fill("black")

    game_screen.draw_self()
    snake.draw_self()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
