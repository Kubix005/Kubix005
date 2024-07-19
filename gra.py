import pygame
pygame.init()
window = pygame.display.set_mode((300,300))
window.fill((255,128,0))
pygame.display.set_caption("Pygame - projekt")
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    