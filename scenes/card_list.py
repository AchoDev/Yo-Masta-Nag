

import pygame, os
from main import WIN

card_width, card_height = 260 / 2, 350 / 2

from cls.Button import Button
from cls.Colors import COL
from cls.Text import Text
from cls.Image import Image
from cls.functions import *

from cls.Container import Container

RETURN_TO_MENU = pygame.USEREVENT + 7
CARD_LIST_LEFT_PRESS = pygame.USEREVENT + 8
CARD_LIST_RIGHT_PRESS = pygame.USEREVENT + 9

class Clickable_Card(Image):
    def __init__(self, xPos, yPos, width, height, image_path):
        super().__init__()

        self.x = xPos
        self.y = yPos
        self.width = width
        self.height = height

        self.is_selected = False
        self.multiplicator = 8
        self.clicked = False

        self.original_position = (0, 0)

        self.set_image(image_path)

    def set_original_pos(self, pos):
        self.original_position = pos

    def draw(self, window):
        super().draw(window)
        m_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] == 1:

            if self.clicked == False:
                if window.get_rect(self).collidepoint(m_pos):

                    self.clicked = True

                    if not self.is_selected:
                        self.is_selected = True

                        self.width *= self.multiplicator
                        self.height *= self.multiplicator

                        self.place_center(WIN)
                    
                        self.update()
                    else:
                        self.is_selected = False

                        self.width /= self.multiplicator
                        self.height /= self.multiplicator

                        self.x = self.original_position[0]
                        self.y = self.original_position[1]

                        self.update()  

        elif pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = False

head_text = Text(10, 10, COL.black.value, 120, "All cards")
head_text.place_center(WIN)
head_text.place_top()

back_button = Button(10, 10, 150, 100, COL.white.value, "<---", 75, RETURN_TO_MENU, 5)

left_button = Button(0, 0, 100, 100, COL.white.value, "<", 75, CARD_LIST_LEFT_PRESS)
right_button = Button(0, 0, 100, 100, COL.white.value, ">", 75, CARD_LIST_RIGHT_PRESS)

# RED CARDS
goblin_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "goblin.jpeg"))
tank_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "broken_tank.jpeg"))
junkie_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "junkie.jpeg"))
ghost_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "lost_ghost.jpeg"))
transition_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "missing_transition.jpeg"))
paralasis_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "red", "sleep_paralysis_demon.jpeg"))

# BLUE CARDS
kuba_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "blue", "kuba_colognalo.jpeg"))
dealer_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "blue", "bubblegum_dealer.jpeg"))
mario_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "blue", "mario.jpeg"))
rejection_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "blue", "rejection.jpeg"))
comedian_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "blue", "stand_up_comedian.jpeg"))

# GREEN CARDS

camera_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "green", "cameraman.jpeg"))
desert_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "green", "desert_bandit.jpeg"))
hell_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "green", "hell_demon.jpeg"))
way_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "green", "no_way.jpeg"))
xray_card = Clickable_Card(100, 100, card_width, card_height, os.path.join("Assets", "Cards", "green", "x_rayvren.jpeg"))

reds = [
    goblin_card,
    tank_card,
    junkie_card,
    ghost_card,
    transition_card,
    paralasis_card
]

blues = [
    kuba_card,
    dealer_card,
    mario_card,
    rejection_card,
    comedian_card
]

greens = [
    camera_card,
    desert_card,
    hell_card,
    way_card,
    xray_card
]



left_button.place_center(WIN)
right_button.place_center(WIN)

left_button.place_left()
right_button.place_right(WIN)

page_index = Container(0)



cards = [
    reds,
    blues,
    greens
]

for list in cards:
    align_grid_center(list, 1000, 1000, WIN, 3)
    set_original_positions(list)

def load_scene():
    WIN.fill(COL.yellow.value)

    WIN.draw_many(cards[page_index.value])

    for card in cards[page_index.value]:
        if card.is_selected:
            WIN.draw_one(card)

    WIN.draw_many((
        left_button,
        right_button,
        back_button
    ))

