from .transform import Transform


class Entity:
    def __init__(self, name: str, transform: Transform, components={}):
        # components
        self._name: str = name
        self._transform: Transform = transform
        self._components = components

    def get_transform(self):
        return self._transform

    def get_position(self):
        return self._transform.get_position()

    def set_position(self, pos):
        return self._transform.set_position(pos)

    def get_position_tuple(self):
        pos = self.get_position()
        return (pos[0], pos[1])
    
