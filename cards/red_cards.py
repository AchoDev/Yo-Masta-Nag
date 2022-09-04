
import os, sys

sys.path.append("..")

from cls.Card import *
from cls.Image import Image
import scenes.game_src.obj as obj




class goblin(Card):
    def __init__(self, draggable):
        image = Image()
        image.set_image(os.path.join("Assets", "Cards", "red", "goblin.jpeg"))
        super().__init__(0, 0, obj.card_width.value, obj.card_height.value, image=image)

        self.name = "goblin"

        self.health = 2
        self.damage = 1
        self.cost = 2

        self.range = attackable.enemy_cards.value
        self.effect = None

class lost_ghost(Card):
    def __init__(self, draggable):
        image = Image()
        image.set_image(os.path.join("Assets", "Cards", "red", "lost_ghost.jpeg"))
        super().__init__(0, 0, obj.card_width.value, obj.card_height.value, image=image)

        self.name = "lost_ghost"

        self.health = 1
        self.damage = 1
        self.cost = 1

        self.range = attackable.enemy_cards.value
        self.effect = None

class broken_tank(Card):
    def __init__(self, draggable):
        image = Image()
        image.set_image(os.path.join("Assets", "Cards", "red", "broken_tank.jpeg"))
        super().__init__(0, 0, obj.card_width.value, obj.card_height.value, image=image)

        self.name = "broken_tank"

        self.health = 10
        self.damage = 0
        self.cost = 0

        self.range = attackable.enemy_cards.value
        self.effect = None

def junkie_effect(attacker, victim):
    if attacker.free_attacks > 0:
        attacker.free_attacks -= 1

class junkie(Card):
    def __init__(self, draggable):
        image = Image()
        image.set_image(os.path.join("Assets", "Cards", "red", "junkie.jpeg"))
        super().__init__(0, 0, obj.card_width.value, obj.card_height.value, image=image)

        self.name = "junkie"

        self.health = 4
        self.damage = 2
        self.cost = 3

        self.range = attackable.enemy_cards.value
        self.effect = junkie_effect

        self.free_attacks = 0
        self.original_cost = self.cost

    def draw(self, window):
        super().draw(window)

        if(self.free_attacks != 0):
            self.cost = 0
        else:
            self.cost = self.original_cost

def mt_effect(attacker, victim):
    for card in attacker.death_list:
        if card == victim:
            return None
        
    victim.damage *= 2
    victim.death_round = obj.current_round.value + 1
    attacker.death_list.append(victim)

class missing_transition(Card):
    def __init__(self, draggable):
        image = Image()
        image.set_image(os.path.join("Assets", "Cards", "red", "missing_transition.jpeg"))
        super().__init__(0, 0, obj.card_width.value, obj.card_height.value, image=image)

        self.name = "missing_transition"

        self.health = 5
        self.damage = 1
        self.cost = 1

        self.death_list = []

        self.range = attackable.enemy_cards.value
        self.effect = mt_effect

    def draw(self, window):
        super().draw(window)

        for card in self.death_list:
            if card.death_round == obj.current_round.value:
                card.health = 0
                self.death_list.remove(card)

