
from .obj import *

def load_game_scene():
    background_image.draw(WIN)

    if is_own_turn.value:
        WIN.draw_one(end_turn_button)
    else:
        WIN.draw_one(enemy_turn_image)

    WIN.draw_many(areas)
    WIN.draw_many(enemy_areas)

    WIN.draw_many(enemy_hand_cards)
    WIN.draw_many(hand_cards)

    for card in active_cards:
        if card.value != None:
            WIN.draw_one(card.value)

    if len(deck_cards) >= 1:
        WIN.draw_one(deck_image)    

    WIN.draw_one(energy_meter_images[energy])
    WIN.draw_one(enemy_energy_meter_images[enemy_energy])

