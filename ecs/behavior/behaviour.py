
from ..entity import Entity


class Behaviour():
    def __init__(self):
        pass

    def update_impl(self, screen, delta_time: float, entity: Entity):
        pass

    def do_update(self, screen, delta_time: float, entity: Entity):
        self.update_impl(screen, delta_time, entity)
