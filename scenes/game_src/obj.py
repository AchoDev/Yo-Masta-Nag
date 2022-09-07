from cls.Container import Container
from cls.Image import Image
from cls.Button import Button
from cls.functions import *
import os 

card_width = Container(45)
card_height = Container(64)

from main import WIN


enemy_hand_cards = []
hand_cards = []

deck_cards = []
enemy_deck_cards = []

active_cards = [
    Container(),
    Container(),
    Container() 
]

enemy_active_cards = [
    Container(),
    Container(),
    Container()
]

areas = []
enemy_areas = []

end_turn_image = Image()
deck_image = Image()

energy_meter_images = []
energy = Container()

enemy_energy_meter_images = []
enemy_energy = Container()


card_combined_width = Container()

background_image = Image()

end_turn_button = Button()
enemy_turn_image = Image()

is_own_turn = Container(True)

current_round = Container(0)

def update_screen():
    card_combined_width.value = WIN.width * 0.2

def reset_board(cards):

    background_image.x = WIN.width
    background_image.y = WIN.height
    
    background_image.set_image(os.path.join("Assets", "Maps", "palace.jpg"))

    for obj in [hand_cards, enemy_hand_cards]:
        align_x(WIN.width * 0.5, obj.value)
        align_center_x(card_combined_width.value, obj)

    for obj in [areas, enemy_areas]:
        align_x(WIN.width * 0.4, obj)
        align_center_x(WIN.width, obj)

    move_many("top", enemy_hand_cards, WIN)
    move_many("bot", hand_cards, WIN)

    

