from typing import List

from .transform import Transform
from .base_renderer import BaseRenderer
import numpy as np


class Entity:
    def __init__(self, name: str, transform: Transform, color: (int, int, int), size: (int, int), behaviours: List, show_name: bool = False):
        self._name: str = name
        self._transform: Transform = transform
        self._color:  (int, int, int) = color
        self._renderer = BaseRenderer(
            color, size, self.get_position_tuple(), name, show_name)
        self._speed_vector: np.ndarray = np.array([0, 0])
        self.behaviours = behaviours
        self.show_name: bool = show_name

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

    def update(self, screen, delta_time: float):
        for b in self.behaviours:
            b.do_update(screen, delta_time, self)
        self.move(delta_time)

    def render(self, screen):
        self._renderer.render(screen)

    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)

    def distance_to_target(self, dst):
        vec = self.get_position() - dst.get_position()
        return np.sqrt(np.sum(vec**2))
