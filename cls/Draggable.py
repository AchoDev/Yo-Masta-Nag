
import pygame

from cls.Colors import COL
from .Window import Window as window, window_ratio
from .Square import Square


class Draggable():
    def __init__(self):
        self.is_dragged = False
        self.is_draggable = True
        self.is_hovered = False


    def drag(self):

        if(self.is_draggable):
            m_pos = pygame.mouse.get_pos()

            if self.is_dragged == True:
                self.x = m_pos[0] - self.__offset[0]
                self.y = m_pos[1] - self.__offset[1]


                if pygame.mouse.get_pressed()[0] == 0:
                    self.is_dragged = False
                    self.drop()

            if window.get_rect(self).collidepoint(m_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    if self.is_hovered == True:
                        self.__offset = (m_pos[0] - self.x, m_pos[1] - self.y)
                        self.is_dragged = True
                    else:
                        pass
                else:
                    self.is_hovered = True
            else:
                self.is_hovered = False
                self.is_dragged = False



        
        