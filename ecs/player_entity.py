
from .entity import Entity
from .transform import Transform
import numpy as np
import random

class PlayerEntity(Entity):
    def __init__(self, speed, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed

    def get_random_direction_vector(self,speed):
        player_pos = np.array([random.random() * 2 - 1, random.random() * 2 - 1])
        return speed * player_pos / np.sqrt(np.sum(player_pos**2))


    def move(self, direction):
        pos = Transform.wrap_toloidal_pos(
            self.get_position() + direction, 1440, 800)
        
        self.set_position(pos)
        return pos
    
    def update(self):
        super().update() 
        self.move(self.get_random_direction_vector(self.speed))
