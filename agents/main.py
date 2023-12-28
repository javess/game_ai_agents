import pygame
import sys
import numpy as np
import random
from ecslib.game.app_state import AppState
from ecslib.entity import Entity
from ecslib.behavior.enemy import EnemyEntity
from ecslib.behavior.player import PlayerEntity
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

player = Entity(name='Player', transform=Transform(np.array([100, 100])), color=(255, 255, 255), size=PLAYER_SIZE, behaviours=[
    PlayerEntity(speed=150)
])
enemy1 = Entity(name='Enemy1', transform=Transform(np.array([800, 600])), color=(255, 0, 0), size=PLAYER_SIZE, behaviours=[
    EnemyEntity(speed=120, target=player, max_acceleration=5)
])
enemy2 = Entity(name='Enemy2', transform=Transform(np.array([400, 600])), color=(0, 255, 0), size=PLAYER_SIZE, behaviours=[
    EnemyEntity(speed=100, target=player, max_acceleration=5)
])

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

    # Limit the FPS by sleeping for the remainder of the frame time
    frame_time = clock.tick(fps)
    time_delta = min(frame_time/1000.0, 0.1)
    app_state.update(screen, time_delta)

    pygame.display.update()
