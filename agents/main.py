import pygame
import sys
import numpy as np
import random
from ecslib.game.app_state import AppState
from ecslib.entity import Entity
from ecslib.behavior.enemy import ChaserBehaviour
from ecslib.behavior.player import RandomWandererBehaviour
from ecslib.transform import Transform


WORLD_WIDTH = 1440
WORLD_HEIGHT = 800
ENEMY_COUNT = 10
PLAYER_SIZE = (15, 15)

# Create a clock object
clock = pygame.time.Clock()

# Set the desired FPS
fps = 60

pygame.init()
screen = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))
app_state = AppState()

player = Entity(name='Player', transform=Transform(np.array([100, 100])), color=(255, 255, 255), size=PLAYER_SIZE, behaviours=[
    RandomWandererBehaviour(speed=150)
])
app_state.add_entity(player)

enemies = []
for i in range(ENEMY_COUNT):
    enemy = Entity(name=f'Enemy-{i}', transform=Transform(np.array([400 + (20 * i), 400 + (25*i)])), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), size=PLAYER_SIZE, behaviours=[
        ChaserBehaviour(speed=15*(i+1), target=player, max_acceleration=5)
    ])
    enemies.append(enemy)
    app_state.add_entity(enemy)


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
