
import pygame
from .draw import draw_scene
from main import WIN

def start():
    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.VIDEORESIZE:
                WIN.videoresize()


        draw_scene()
        pygame.display.update()
