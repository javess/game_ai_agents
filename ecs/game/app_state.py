from typing import List, Type
from ..entity import Entity


class AppState:
    def __init__(self):
        self.entities: List[Type[Entity]] = []

    def update(self, screen, delta_time) -> None:
        for entity in self.entities:
            entity.update(screen, delta_time)
        for entity in self.entities:
            entity.render(screen)

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)
