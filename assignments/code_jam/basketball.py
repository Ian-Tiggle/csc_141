# Basketball
# Ian Tiggle
# Put the basketball on the screen

import pygame
# import sys
# C:\Users\Dave\OneDrive\Albright\CSC141\super_hero_game\images\basketball.png
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1240,700))
my_image = pygame.image.load("C:/csc_141/assignments/code_jam/images/Star-Lord Deluxe Avatar.png").convert_alpha()
image_rect = my_image.get_rect(center =(620, 350))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        image_rect.x += 10
    if keys[pygame.K_s]:
        image_rect.y += 10
    if keys[pygame.K_w]:
        image_rect.y -= 10
    if keys[pygame.K_a]:
        image_rect.x -= 10
        
    # if image_rect.x > screen.get_width():
    #     image_rect.x = 0
    screen.blit(my_image, image_rect)
    pygame.display.flip()
    clock.tick(120)
