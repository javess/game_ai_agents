import pygame
import sys
import numpy as np
import random
from game.app_state import AppState
from ecslib.entity import Entity
from ecslib.enemy_entity import EnemyEntity
from ecslib.player_entity import PlayerEntity
from ecslib.transform import Transform


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

player = PlayerEntity(speed= 50, name = 'Player', transform = Transform(np.array([100, 100])), color = (255, 255, 255), size = PLAYER_SIZE)
enemy1 = EnemyEntity(target= player, speed= 1, name = 'Enemy1', transform = Transform(np.array([800, 600])), color = (255, 0, 0), size = PLAYER_SIZE)
enemy2 = EnemyEntity(target= player, speed= 2, name = 'Enemy2', transform = Transform(np.array([400, 600])), color = (0, 255, 0), size = PLAYER_SIZE)

app_state = AppState()
app_state.add_entity(player)
app_state.add_entity(enemy1)
app_state.add_entity(enemy2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # redraw enemies
    screen.fill((0, 0, 0))

    app_state.update(screen)


    # player_velocity = get_random_direction_vector(PLAYER_SPEED)
    # player.set_position(wrap_toloidal_pos(
    #      player.get_position() + player_velocity, WORLD_WIDTH, WORLD_HEIGHT))

    # player_pos = player.get_position_tuple();
    # player_rect.x = player_pos[0]
    # player_rect.y = player_pos[1]

    pygame.display.update()
    # Limit the FPS by sleeping for the remainder of the frame time
    clock.tick(fps)
