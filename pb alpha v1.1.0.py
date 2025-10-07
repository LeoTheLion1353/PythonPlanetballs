import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("DSE Alpha v1.1.0")

font = pygame.font.SysFont(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 242, 0), (320, 240), 100)

    left_eye_rect = (260, 200, 50, 50)
    pygame.draw.arc(screen, (0, 0, 0), left_eye_rect, 0, math.pi, 5)

    right_eye_rect = (330, 200, 50, 50)
    pygame.draw.arc(screen, (0, 0, 0), right_eye_rect, 0, math.pi, 5)

    pygame.draw.circle(screen, (255, 127, 0), (600, 240), 100)

    left_eye_rect = (560, 200, 50, 50)
    pygame.draw.arc(screen, (0, 0, 0), left_eye_rect, 0, math.pi, 5)

    right_eye_rect = (640, 200, 50, 50)
    pygame.draw.arc(screen, (0, 0, 0), right_eye_rect, 0, math.pi, 5)
    
    text_surface = font.render("The August Overhaul", True, (255, 255, 255))
    text_rect = text_surface.get_rect(topright=(640 - 10, 10))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("G Type Star", True, (255, 255, 255))
    text_rect = text_surface.get_rect(midtop=(300, 10))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("K Type Star", True, (255, 255, 255))
    text_rect = text_surface.get_rect(topright=(600, 10))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()
