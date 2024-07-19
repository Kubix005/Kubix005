import pygame
import sys

pygame.init()
window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Pygame - projekt")

gracz = pygame.Rect(50, 50, 50, 50)
gracz_kolor = (0, 0, 0)
clock = pygame.time.Clock()
rect_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and gracz.top > 0:
        gracz.y -= rect_speed
    if keys[pygame.K_s] and gracz.bottom < window.get_height():
        gracz.y += rect_speed
    if keys[pygame.K_a] and gracz.left > 0:
        gracz.x -= rect_speed
    if keys[pygame.K_d] and gracz.right < window.get_width():
        gracz.x += rect_speed

    window.fill((255, 128, 0))
    pygame.draw.rect(window, gracz_kolor, gracz)
    pygame.display.update()
    clock.tick(60)
