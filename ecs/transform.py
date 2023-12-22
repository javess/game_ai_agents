import numpy as np


class Transform:
    def __init__(self, pos):
        self._pos = pos

    def get_position(self):
        return self._pos

    def set_position(self, pos):
        self._pos = pos
