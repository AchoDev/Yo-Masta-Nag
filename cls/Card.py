import pygame

import sys, os, enum
from .Colors import COL
from .Text import Text
from .GameObject import GameObject
from .functions import sync_transform

sys.path.append("..")

from scenes import game

class Card(GameObject):

    is_dragged = False
    __offset = (0, 0)
    hand_pos = (0, 0)
    draw_text = True

    def __init__(self, xPos, yPos, width, height, draggable = False, event=None, state = 0, image=None):
        
        super().__init__(xPos, yPos, width, height)

        self.event = event
        self.is_draggable = draggable 
        self.is_hovered = False

        self.current_state = state

        self.health = 3
        self.damage = 1
        self.cost = 1

        self.lives = 2
        self.is_dead = False

        self.__original_pos = (xPos, yPos)
        self.__image = image

        self.__image.update()

    def set_image(self, image):
        self.__image = image

    def resize(self, width, height):
        super().resize(width, height)
        self.__image.resize(self.width, self.height)
        self.update_image()
        
    def set_original_pos(self, pos):
        self.__original_pos = pos

    def get_offset(self):
        return self.__offset

    def get_original_pos(self):
        return self.__original_pos

    def return_to_hand(self):
        self.x = self.hand_pos[0]
        self.y = self.hand_pos[1]
            
    def update_image(self):
        sync_transform(self, self.__image)
        self.__image.update()

    def set_hand_pos(self, pos):
        self.hand_pos = pos

    def draw(self, window):

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

            # if pygame.mouse.get_pressed()[0] == 1:
            #     if window.get_rect(self).collidepoint(m_pos):
            #         self.__offset = (m_pos[0] - self.x, m_pos[1] - self.y)
            #         self.is_dragged = True    


        # window.draw_rect(self, self.color)
        sync_transform(self, self.__image)
        self.__image.draw(window)

        if self.draw_text:
            health_text = Text(self.x, self.y, COL.black.value, 40, "health:" + str(self.health))
            lives_text = Text(self.x, self.y + 100, COL.black.value, 40, "lives:" + str(self.lives))
            cost_text = Text(self.x, self.y + 50, COL.black.value, 40, "cost:" + str(self.cost))
            damage_text = Text(self.x, self.y + 150, COL.black.value, 40, "damage:" + str(self.damage))

            health_text.draw(window)
            lives_text.draw(window)
            cost_text.draw(window)
            damage_text.draw(window)

    def drop(self):
        # pygame.event.post(pygame.event.Event(self.event))

        game.drop_card(self)

    def return_to_original_position(self):
        self.x = self.__original_pos[0]
        self.y = self.__original_pos[1]

    

class attackable(enum.Enum):
    pacifist = 0
    own_cards = 1
    enemy_cards = 2
    all_cards = 3