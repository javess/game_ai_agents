
from ..entity import Entity
from ..transform import Transform
import numpy as np
import random

class PlayerEntity(Entity):
    def __init__(self, speed, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.max_turn_angle = 10

    def rotate_vector(self, vector, angle_degrees):
        # Convert angle to radians
        angle_radians = np.radians(angle_degrees)

        # Define the 2D rotation matrix
        rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                                    [np.sin(angle_radians), np.cos(angle_radians)]])

        # Rotate the vector
        rotated_vector = np.dot(rotation_matrix, vector)

        return rotated_vector

    def get_random_direction_vector(self,speed):
        random_float_range = random.uniform(-self.max_turn_angle, self.max_turn_angle)
        direction = self.rotate_vector(self._speed_vector, random_float_range)
        return speed * direction / np.sqrt(np.sum(direction**2))

    def update_speed_vector(self, direction):
        self._speed_vector = direction
    
    def update(self, delta_time: float):
        self.update_speed_vector(self.get_random_direction_vector(self.speed))
        super().update(delta_time) 
