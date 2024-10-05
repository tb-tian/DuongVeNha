import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1000, 707))
pygame.display.set_caption('DuongVeNha')
clock = pygame.time.Clock()

background_surface = pygame.image.load('./assets/Background.png').convert()
background_surface = pygame.transform.scale(background_surface, (1000, 707))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))
    pygame.display.update()
    clock.tick(60) 