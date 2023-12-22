import pygame

class BaseRenderer:
    def __init__(self, color: (int, int, int), size: (int, int), pos: (int, int)):
        self.color: (int, int, int) = color
        self.size: (int, int) = size
        self.player_rect = pygame.Rect(pos, size)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.player_rect)

    def set_pos(self, pos):
        self.player_rect.x = pos[0]
        self.player_rect.y = pos[1]

