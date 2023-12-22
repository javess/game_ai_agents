import numpy as np

class Transform:
    def __init__(self, pos:np.ndarray):
        self._pos:np.ndarray[(int, int)] = pos

    def get_position(self) -> np.ndarray:
        return self._pos

    def set_position(self, pos: np.ndarray):
        self._pos = pos

    @staticmethod
    def wrap_toloidal_pos(pos, width, height):
        return np.array([pos[0] % width if pos[0] > 0 else width-1, pos[1] % height if pos[1] > 0 else height-1])
