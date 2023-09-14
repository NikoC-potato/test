import pygame
import sys
white = (255, 255, 255)
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("IA game")
pygame.display.flip()
clock = pygame.time.Clock()
color = (255, 255, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.line(screen, white, [600,200], [600, 400], 6)
    pygame.draw.line(screen, white, [200,200], [200, 400], 6)


    pygame.display.flip()
    clock.tick(60)
pygame.quit()