
import pygame
from .GameObject import GameObject

class Square(GameObject):
    def __init__(self, xPos, yPos, width, height, color, border_radius=0, hollow=False):
        super().__init__(xPos, yPos, width, height)

        self.color = color
        self.border_radius = border_radius
        self.is_hollow = hollow

    def draw(self, window):
        window.draw_rect(self, self.color)