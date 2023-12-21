import pygame
import sys
import numpy as np
import time
import random


def get_random_direction_vector(speed):
    player_pos = np.array([random.random() * 2 - 1, random.random() * 2 - 1])
    return speed * player_pos / np.sqrt(np.sum(player_pos**2))


def wrap_toloidal_pos(pos, width, height):
    return np.array([pos[0] % width if pos[0] > 0 else width-1, pos[1] % height if pos[1] > 0 else height-1])


def move_enemy(player_pos, enemy_pos, enemy, speed):
    target_move = player_pos - enemy_pos
    normalized_move = (target_move / np.sqrt(np.sum(target_move**2))) * speed
    enemy_pos = wrap_toloidal_pos(
        enemy_pos + normalized_move, WORLD_WIDTH, WORLD_HEIGHT)
    enemy.x = enemy_pos[0]
    enemy.y = enemy_pos[1]
    return (enemy, enemy_pos)


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

player_pos = np.array([50, 50])
player = pygame.Rect((player_pos[0], player_pos[1]), PLAYER_SIZE)

enemy_pos = np.array([800, 600])
enemy = pygame.Rect((enemy_pos[0], enemy_pos[1]), PLAYER_SIZE)

enemy_pos_2 = np.array([400, 600])
enemy_2 = pygame.Rect((enemy_pos_2[0], enemy_pos_2[1]), PLAYER_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.draw.rect(screen, (0, 255, 0), enemy_2)

    (enemy, enemy_pos) = move_enemy(
        player_pos, enemy_pos, enemy, CHASER_SPEED * 2)
    (enemy_2, enemy_pos_2) = move_enemy(
        player_pos, enemy_pos_2, enemy_2, CHASER_SPEED)

    player_velocity = get_random_direction_vector(PLAYER_SPEED)
    player_pos = wrap_toloidal_pos(
        player_pos + player_velocity, WORLD_WIDTH, WORLD_HEIGHT)

    player.x = player_pos[0]
    player.y = player_pos[1]

    pygame.display.update()
    # Limit the FPS by sleeping for the remainder of the frame time
    clock.tick(fps)
