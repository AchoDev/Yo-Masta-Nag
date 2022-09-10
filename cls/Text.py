
import pygame
from cls.GameObject import GameObject

pygame.font.init()

class Text(GameObject):
    def __init__(self, xPos, yPos, width, color, text):
        super().__init__(xPos, yPos)
        
        self.font = pygame.font.SysFont('ebrima', round(width // 10))
        self.text = text 
        self.color = color

        self.width = 1920

        self.__set_size()
        
    def __set_size(self):
        self.width = self.__get_body().get_width()
        self.height = self.__get_body().get_height()

    def __get_body(self):

        self.font = pygame.font.SysFont('ebrima', round(self.width // 10))
        return self.font.render(self.text, 1, self.color)

    def draw(self, window):
        text = self.font.render(self.text, 1, self.color)
        window.win.blit(self.__get_body(), (self.x, self.y))

    def change_text(self, text):
        self.text = text