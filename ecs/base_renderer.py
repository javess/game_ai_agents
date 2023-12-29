import pygame


class BaseRenderer:
    def __init__(self, color: (int, int, int), size: (int, int), pos: (int, int), name: str, show_name: bool):
        self.color: (int, int, int) = color
        self.size: (int, int) = size
        self.player_rect = pygame.Rect(pos, size)
        self.font_size = 18
        self.font = pygame.font.Font(None, self.font_size)
        self.name: str = name
        self.show_name: bool = show_name

    def render(self, screen):
        if self.show_name:
            # Render the text
            text_surface = self.font.render(self.name, True, self.color)
            # Get the rectangle of the text surface
            text_rect = text_surface.get_rect()
            text_rect.center = (self.player_rect.x + 10,
                                self.player_rect.y - 15)
            # Blit the text surface onto the screen
            screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, self.color, self.player_rect)

    def set_pos(self, pos):
        self.player_rect.x = pos[0]
        self.player_rect.y = pos[1]
