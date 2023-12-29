import pygame
import sys
import numpy as np
import random
from ecslib.game.app_state import AppState
from ecslib.entity import Entity
from ecslib.behavior.blinker import BlinkerBehaviour
from ecslib.behavior.chaser import ChaserBehaviour
from ecslib.behavior.wanderer import RandomWandererBehaviour
from ecslib.behavior.avoider import AvoiderBehaviour
from ecslib.transform import Transform


WORLD_WIDTH = 1440
WORLD_HEIGHT = 800
ENEMY_COUNT = 10
PLAYER_SIZE = (15, 15)
BASE_SPEED = 200
# Create a clock object
clock = pygame.time.Clock()

# Set the desired FPS
fps = 90

pygame.init()
screen = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))
app_state = AppState()

target = Entity(name='Target', transform=Transform(np.array([WORLD_WIDTH/2, WORLD_HEIGHT/2])), color=(0, 255, 0), size=PLAYER_SIZE, show_name=True, behaviours=[
])
app_state.add_entity(target)

player = Entity(name='Player', transform=Transform(np.array([100, 100])), color=(255, 255, 255), size=PLAYER_SIZE, show_name=True, behaviours=[
    RandomWandererBehaviour(speed=BASE_SPEED/2),
    ChaserBehaviour(speed=BASE_SPEED*2, target=target, max_acceleration=5),
])
app_state.add_entity(player)

enemies = []
for i in range(ENEMY_COUNT):
    enemy = Entity(name=f'Enemy-{i}', transform=Transform(np.array([400 + (20 * i), 400 + (25*i)])), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), size=PLAYER_SIZE, behaviours=[
        ChaserBehaviour(speed=BASE_SPEED/2, target=player, max_acceleration=5),
        RandomWandererBehaviour(speed=BASE_SPEED, max_turn_angle=20)
    ])
    enemies.append(enemy)
    app_state.add_entity(enemy)

for e in enemies:
    e.add_behaviour(
        AvoiderBehaviour(targets=enemies, speed=BASE_SPEED/2, max_distance=60)
    )

player.add_behaviour(AvoiderBehaviour(
    targets=enemies, speed=BASE_SPEED, max_distance=100, show_radius=True))
target.add_behaviour(BlinkerBehaviour(
    target=player, radius=30, map_width=WORLD_WIDTH, map_height=WORLD_HEIGHT))

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
