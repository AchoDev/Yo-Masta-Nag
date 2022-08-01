
import os, sys

sys.path.append("..")

from cls.Card import *
from cls.Image import Image
from scenes.game import card_height, card_width


def kuba_colognalo_effect(attacker, victim):
    victim.health += 2

class kuba_colognalo(Card):
    def __init__(self, draggable):
        image = Image()
        image.set_image(os.path.join("Assets", "Cards", "blue" ,"kuba_colognalo.jpeg"))
        super().__init__(0, 0, card_width, card_height, image=image)

        self.name = "kuba_colognalo"

        self.is_draggable = draggable

        self.health = 1
        self.damage = 0
        self.cost = 2

        self.range = attackable.own_cards.value
        self.effect = kuba_colognalo_effect

def bd_effect(attacker, victim):
    
    for card in attacker.high_list:
        if card == victim:
            return None
        
    victim.health *= 2
    victim.damage *= 2

    if victim.name == "junkie":
        victim.free_attacks = 2

    attacker.high_list.append(victim)

class bubblegum_dealer(Card):
    def __init__(self, draggable):
        image = Image()
        image.set_image(os.path.join("Assets", "Cards", "blue", "bubblegum_dealer.jpeg"))
        super().__init__(0, 0, card_width, card_height, image=image)

        self.name = "bubblegum_dealer"

        self.is_draggable = draggable

        self.health = 3
        self.damage = 0
        self.cost = 3

        self.range = attackable.own_cards.value
        self.effect = bd_effect

        self.high_list = []