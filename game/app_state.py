from typing import List, Type
from ecslib.entity import Entity

class AppState:
    def __init__(self):
        self.entities: List[Type[Entity]] = []

    def update(self, screen) -> None:
        for entity in self.entities:
            entity.update()
        for entity in self.entities:
            entity.render(screen)
    
    def add_entity(self, entity:Entity) -> None:
        self.entities.append(entity)