
from ..entity import Entity
from .behaviour import Behaviour
import numpy as np


class ChaserBehaviour(Behaviour):
    def __init__(self, target: Entity, speed: float, max_acceleration: float, **kwargs):
        super().__init__(**kwargs)
        self.target: Entity = target
        self.speed: float = speed
        self.max_acceleration: float = max_acceleration

    def update_speed_vector(self, player, entity: Entity):
        acceleration_vector = player.get_position() - entity.get_position()
        normalized_acceleration_vector = (
            acceleration_vector / np.sqrt(np.sum(acceleration_vector**2))) * self.max_acceleration
        new_speed_vector = entity._speed_vector + normalized_acceleration_vector
        speed_magnitude = np.sum(new_speed_vector**2)
        if (speed_magnitude > self.speed):
            entity._speed_vector = (
                new_speed_vector / np.sqrt(np.sum(new_speed_vector**2))) * self.speed
        else:
            entity._speed_vector = new_speed_vector

    def update_impl(self, delta_time: float, entity: Entity):
        self.update_speed_vector(self.target, entity)
