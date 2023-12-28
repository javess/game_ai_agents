
from ..entity import Entity


class Behaviour():
    def __init__(self):
        pass

    def update_impl(self, delta_time: float):
        pass

    def do_update(self, delta_time: float, entity: Entity):
        self.update_impl(delta_time, entity)
