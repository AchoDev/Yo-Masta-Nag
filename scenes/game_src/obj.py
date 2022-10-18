
from cls import *
import os, random

from.convert_cards import convert_card

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

areas = [
    Square(0, 0, card_width.value, card_height.value, COL.green.value, 1, True),
    Square(0, 0, card_width.value, card_height.value, COL.green.value, 1, True),
    Square(0, 0, card_width.value, card_height.value, COL.green.value, 1, True)
]
enemy_areas = [
    Square(0, 0, card_width.value, card_height.value, COL.green.value, 1, True),
    Square(0, 0, card_width.value, card_height.value, COL.green.value, 1, True),
    Square(0, 0, card_width.value, card_height.value, COL.green.value, 1, True)

]

end_turn_image = Image()
end_turn_image.set_image(os.path.join("Assets", "UI", "palace_end_turn.png"))

deck_image = Image()
deck_image.set_image(os.path.join("Assets", "Cards", "card_back.png"))

energy = Container(3)
enemy_energy = Container(3)

energy_meter_images = [
    Image().with_args(700, 100, 200, 150), 
    Image().with_args(700, 100, 200, 150), 
    Image().with_args(700, 100, 200, 150), 
    Image().with_args(700, 100, 200, 150)
]

enemy_energy_meter_images = [
    Image().with_args(500, 100, 200, 150), 
    Image().with_args(500, 100, 200, 150), 
    Image().with_args(500, 100, 200, 150), 
    Image().with_args(500, 100, 200, 150)
]

for i in range(4):
    energy_meter_images[i].set_image(os.path.join("Assets", "UI", f"palace_energy_{str(i)}.png"))
    enemy_energy_meter_images[i].set_image(os.path.join("Assets", "UI", f"palace_energy_{str(i)}.png"))



card_combined_width = Container()

background_image = Image()

END_TURN = pygame.USEREVENT + 40

enemy_turn_image = Image()
enemy_turn_image.set_image(os.path.join("Assets", "UI", "palace_enemy_turn.png"))


end_turn_button = Button().image_button(100, 100, 100, 100, END_TURN, enemy_turn_image)


is_own_turn = Container(True)

current_round = Container(0)

def update_screen():
    card_combined_width.value = WIN.width * 0.2

def reset_board(cards):

    for card in cards:
        c = convert_card(card)
        deck_cards.append(c)
        enemy_deck_cards.append(c) #! ENEMY HAS SAME DECK AS YOU WIP

    for i in range(3):
        def get_random(list):
            return list[random.randint(0, len(list) - 1)]

        random_card = get_random(deck_cards)
        random_enemy_card = get_random(enemy_deck_cards)

        hand_cards.append(random_card)
        enemy_hand_cards.append(random_enemy_card)

        deck_cards.remove(random_card)
        enemy_deck_cards.remove(random_enemy_card)

    card_combined_width.value = 0
    for card in hand_cards:
        card_combined_width.value += card.width


    background_image.x = 1920
    background_image.y = 1080
    
    background_image.set_image(os.path.join("Assets", "Maps", "palace.jpg"))

    for obj in [hand_cards, enemy_hand_cards]:
        align_x(WIN.width * 0.5, obj)
        align_center_x(card_combined_width.value, obj)

    for obj in [areas, enemy_areas]:
        align_x(WIN.width * 0.4, obj)
        align_center_x(WIN.width, obj)

    move_many("top", enemy_hand_cards, WIN)
    move_many("bot", hand_cards, WIN)

    

