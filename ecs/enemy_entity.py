
from .entity import Entity
from .transform import Transform
import numpy as np


class EnemyEntity(Entity):
    def __init__(self, target:Entity, speed, **kwargs):
        super().__init__(**kwargs)
        self.target: Entity = target
        self.speed = speed


    def move_enemy(self, player, speed):
        target_move = player.get_position() - self.get_position()
        normalized_move = (target_move / np.sqrt(np.sum(target_move**2))) * speed
        enemy_pos = Transform.wrap_toloidal_pos(
            self.get_position() + normalized_move, 1440, 800)
        
        self.set_position(enemy_pos)
        return enemy_pos
    
    def update(self):
        super().update()    
        self.move_enemy(self.target, self.speed)
