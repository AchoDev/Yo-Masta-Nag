
from .obj import *

def load_game_scene():
    background_image.draw(WIN)

    if is_own_turn.value:
        WIN.draw_one(end_turn_button, 1920)
    else:
        WIN.draw_one(enemy_turn_image, 1920)

    WIN.draw_many(areas, 1920)
    WIN.draw_many(enemy_areas, 1920)

    WIN.draw_many(enemy_hand_cards, 1920)
    WIN.draw_many(hand_cards, 1920)

    for card in active_cards:
        if card.value != None:
            WIN.draw_one(card.value, 1920)

    if len(deck_cards) >= 1:
        WIN.draw_one(deck_image, 1920)

    WIN.draw_one(energy_meter_images[energy.value], 1920)
    WIN.draw_one(enemy_energy_meter_images[enemy_energy.value], 1920)

