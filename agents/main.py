import pygame
import sys
import numpy as np
import time
import random


import inspect
from ecslib.entity import Entity
from ecslib.transform import Transform


def get_random_direction_vector(speed):
    player_pos = np.array([random.random() * 2 - 1, random.random() * 2 - 1])
    return speed * player_pos / np.sqrt(np.sum(player_pos**2))


def wrap_toloidal_pos(pos, width, height):
    return np.array([pos[0] % width if pos[0] > 0 else width-1, pos[1] % height if pos[1] > 0 else height-1])


def move_enemy(player, enemy, enemy_rect, speed):
    target_move = player.get_position() - enemy.get_position()
    normalized_move = (target_move / np.sqrt(np.sum(target_move**2))) * speed
    enemy_pos = wrap_toloidal_pos(
        enemy.get_position() + normalized_move, WORLD_WIDTH, WORLD_HEIGHT)
    
    enemy.set_position(enemy_pos)

    enemy_rect.x = enemy_pos[0]
    enemy_rect.y = enemy_pos[1]
    return enemy_rect


WORLD_WIDTH = 1440
WORLD_HEIGHT = 800
PLAYER_SIZE = (15, 15)
PLAYER_SPEED = 50
CHASER_SPEED = 1

# Create a clock object
clock = pygame.time.Clock()

# Set the desired FPS
fps = 60

pygame.init()
screen = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))

player = Entity('Player1', Transform(np.array([50, 50])))
player_rect = pygame.Rect(player.get_position_tuple(), PLAYER_SIZE)

enemy1 = Entity('Enemy1', Transform(np.array([800, 600])))
enemy_1_rect = pygame.Rect(enemy1.get_position_tuple(), PLAYER_SIZE)

enemy2 = Entity('Enemy2', Transform(np.array([400, 600])))
enemy_2_rect = pygame.Rect(enemy2.get_position_tuple(), PLAYER_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # redraw enemies
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player_rect)
    pygame.draw.rect(screen, (255, 0, 0), enemy_1_rect)
    pygame.draw.rect(screen, (0, 255, 0), enemy_2_rect)

    enemy_1_rect = move_enemy(
        player, enemy1, enemy_1_rect, CHASER_SPEED * 2)
    enemy_2_rect = move_enemy(
        player, enemy2, enemy_2_rect, CHASER_SPEED)

    player_velocity = get_random_direction_vector(PLAYER_SPEED)
    player.set_position(wrap_toloidal_pos(
         player.get_position() + player_velocity, WORLD_WIDTH, WORLD_HEIGHT))

    player_pos = player.get_position_tuple();
    player_rect.x = player_pos[0]
    player_rect.y = player_pos[1]

    pygame.display.update()
    # Limit the FPS by sleeping for the remainder of the frame time
    clock.tick(fps)
