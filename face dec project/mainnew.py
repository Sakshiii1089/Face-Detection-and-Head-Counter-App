import pygame
pygame.init()

window=pygame.display.set_mode((1200,700))

pygame.display.set_caption("Face Detection App")

start=True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start=False
    pygame.display.update()  