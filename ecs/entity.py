from typing import List, Type
from .transform import Transform
from .base_renderer import BaseRenderer
import numpy as np


class Entity:
    def __init__(self, name: str, transform: Transform, color: (int, int, int), size: (int, int), behaviours: List):
        self._name: str = name
        self._transform: Transform = transform
        self._renderer = BaseRenderer(color, size, self.get_position_tuple())
        self._speed_vector:np.ndarray = np.array([100, 0])
        self.behaviours = behaviours

    def get_transform(self) -> Transform:
        return self._transform

    def get_position(self) -> np.ndarray:
        return self._transform.get_position()

    def set_position(self, pos) -> None:
        self._renderer.set_pos(pos)
        self._transform.set_position(pos)

    def get_position_tuple(self) -> (int, int):
        pos = self.get_position()
        return (pos[0], pos[1])
    
    def move(self, delta_time: float):
        enemy_pos = Transform.wrap_toloidal_pos(
            self.get_position() + self._speed_vector*delta_time, 1440, 800)
        self.set_position(enemy_pos)
    

    def update(self, delta_time: float):
        for b in self.behaviours:
            b.do_update(delta_time, self)
        self.move(delta_time)

    def render(self, screen):
        self._renderer.render(screen, self._name);
    
