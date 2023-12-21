import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = pygame.Rect(50, 50, 50, 50)
enemy = pygame.Rect(400, 300, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), player)
        pygame.draw.rect(screen, (255, 0, 0), enemy)
        speed = 1

        if enemy.x < player.x:
            enemy.x += speed
        elif enemy.x > player.x:
            enemy.x -= speed

        if enemy.y < player.y:
            enemy.y += speed
        elif enemy.y > player.y:
            enemy.y -= speed
        pygame.display.update()
