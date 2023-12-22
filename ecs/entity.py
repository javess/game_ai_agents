from .transform import Transform
from .base_renderer import BaseRenderer
import numpy as np


class Entity:
    def __init__(self, name: str, transform: Transform, color: (int, int, int), size: (int, int)):
        self._name: str = name
        self._transform: Transform = transform
        self._renderer = BaseRenderer(color, size, self.get_position_tuple())

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
    
    def update(self):
        pass

    def render(self, screen):
        self._renderer.render(screen);
    
