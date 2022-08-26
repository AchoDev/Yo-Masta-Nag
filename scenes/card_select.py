
import os
from cls.Button import Button
import main
import pygame


from cls.Image import Image
from cls.Square import Square
from cls.Colors import COL
from cls.functions import *

card_width, card_height = 260 / 2, 350 / 2

class Selectable_Card(Image):
    def __init__(self, xPos, yPos, width, height, image_path):
        super().__init__()

        self.x = xPos
        self.y = yPos
        self.width = width
        self.height = height

        self.is_selected = False
        self.clicked = False

        self.iw = 10 # iw -> indicator width

        self.indicator = Square(xPos - self.iw, yPos - self.iw, width + self.iw * 2, height + self.iw * 2, COL.green.value, 2)
        self.set_image(image_path)

    def set_original_pos(self, pos):
        self.original_position = pos

    def draw(self, window):

        sync_position(self, self.indicator)

        self.indicator.x -= self.iw
        self.indicator.y -= self.iw

        if self.is_selected:
            main.WIN.draw_rect(self.indicator, self.indicator.color)
        super().draw(window)


        m_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] == 1:

            if self.clicked == False:
                if window.get_rect(self).collidepoint(m_pos):

                    self.clicked = True
                    
                    if self.is_selected == True:
                        self.is_selected = False
                    else:
                        self.is_selected = True
        else:
            self.clicked = False


tank_select = Selectable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "broken_tank.jpeg"))
goblin_select = Selectable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "goblin.jpeg"))
junkie_select = Selectable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "junkie.jpeg"))
ghost_select = Selectable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "lost_ghost.jpeg"))
transition_select = Selectable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "missing_transition.jpeg"))
passionate_icecream_eater = Selectable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "passionate_icecream_eater.jpeg"))
paralysis_select = Selectable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "sleep_paralysis_demon.jpeg"))

reds = [
    tank_select,
    goblin_select,
    junkie_select,
    ghost_select,
    transition_select,
    passionate_icecream_eater,
    paralysis_select
]

align_grid_center(reds, 1000, 1000, main.WIN, 3)

START_GAME_EVENT = pygame.USEREVENT + 20

start_button = Button(0, 0, 150, 50, COL.red.value, "START GAME", 75, START_GAME_EVENT)
start_button.place_center(main.WIN)

def load_scene():
    main.WIN.fill(COL.yellow.value)
    main.WIN.draw_many(reds)

    main.WIN.draw_one(start_button)
    