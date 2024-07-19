import pygame
import sys

pygame.init()
wysokosc = 300
dlugosc = 300
window = pygame.display.set_mode((wysokosc,dlugosc))
pygame.display.set_caption("Pygame - projekt")

gracz_x = 50
gracz_y = 50
poprawne_x = int(dlugosc / 2 - gracz_x / 2)
poprawne_y = int(wysokosc / 2 - gracz_y / 2)
gracz = pygame.Rect(poprawne_x, poprawne_y, gracz_x, gracz_y)
gracz_kolor = (0, 0, 0)
clock = pygame.time.Clock()
gracz_szybkosc = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and gracz.top > 0:
        gracz.y -= gracz_szybkosc
    if keys[pygame.K_s] and gracz.bottom < window.get_height():
        gracz.y += gracz_szybkosc
    if keys[pygame.K_a] and gracz.left > 0:
        gracz.x -= gracz_szybkosc
    if keys[pygame.K_d] and gracz.right < window.get_width():
        gracz.x += gracz_szybkosc

    window.fill((255, 128, 0))
    pygame.draw.rect(window, gracz_kolor, gracz)
    pygame.display.update()
    clock.tick(60)
