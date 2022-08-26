
import pygame
import random, time, os, sys
# from cls import COL, align_x, move_bottom, align_center, set_hand_positions, set_original_positions, check_collision, move_top


from cls.Container import Container

from cls.Window import Window
from cls.Button import Button
from cls.Card import *
from cls.Colors import COL
from cls.functions import *
from cls.GameObject import GameObject
from cls.Point import Point
from cls.Text import Text
from cls.Image import Image
from cls.Square import Square



from main import WIN, FPS
from Animations.__class import *
sys.path.append("..")


card_width, card_height = Container(260), Container(350) # Container(260 / (WIN.height / 200)), Container(350 / (WIN.height / 200))

from cards.red_cards import *
from cards.blue_cards import *


CARD_DROP = pygame.USEREVENT + 2
END_TURN = pygame.USEREVENT + 3

PLAYER_WON = pygame.USEREVENT + 4
ENEMY_WON = pygame.USEREVENT + 5

MAP_NAME = Container(None)

background_image = Image.with_args(0, 0, WIN.width, WIN.height)

# CARD STATES:
# 0: in hand
# 1: on table active
# 2: dead
# 3: stil in deck

# card_image = Image()
# card_image.set_image(os.path.join("Assets", "Cards", "goblin.jpeg"))

# card1 = goblin(0, 0, card_width, card_height, draggable=True, event=CARD_DROP, image=card_image)
# card2 = goblin(0, 0, card_width, card_height, draggable=True, event=CARD_DROP, image=card_image)
# card3 = kuba_colognalo(0, 0, card_width, card_height, draggable=True, event=CARD_DROP, image=card_image)

selected_cards = [
    junkie(True),
    bubblegum_dealer(True),
    missing_transition(True),
    broken_tank(True),
    kuba_colognalo(True),
    lost_ghost(True),
    goblin(True)
]

hand_cards = []

for i in range(3):
    rand_card = None

    rand_card = selected_cards[random.randint(0, len(selected_cards) - 1)]

    hand_cards.append(rand_card)
    selected_cards.remove(rand_card)

deck_cards = selected_cards.copy()

# card1 = junkie(draggable=True)
# card2 = bubblegum_dealer(draggable=True)
# card3 = missing_transition(draggable=True)

# enemy_card1 = goblin(0, 0, card_width, card_height, draggable=False, event=CARD_DROP, image=card_image)
# enemy_card2 = goblin(0, 0, card_width, card_height, draggable=False, event=CARD_DROP, image=card_image)
# enemy_card3 = goblin(0, 0, card_width, card_height, draggable=False, event=CARD_DROP, image=card_image)

enemy_card1 = goblin(draggable=False)
enemy_card2 = goblin(draggable=False)
enemy_card3 = goblin(draggable=False)

drop_area1 = Square(0, (WIN.height // 2), card_width.value, card_height.value, COL.green.value, border_radius=10, hollow=True)
drop_area2 = Square(0, (WIN.height // 2), card_width.value, card_height.value, COL.green.value, border_radius=10, hollow=True)
drop_area3 = Square(0, (WIN.height // 2), card_width.value, card_height.value, COL.green.value, border_radius=10, hollow=True)

# enemy_drop_area1 = pygpp.Point(0, (WIN.height // 2) + card_height)
# enemy_drop_area2 = pygpp.Point(0, (WIN.height // 2) + card_height)
# enemy_drop_area3 = pygpp.Point(0, (WIN.height // 2) + card_height)

enemy_drop_area1 = Square(0, (WIN.height // 2) - card_height.value, card_width.value, card_height.value, COL.red.value, border_radius=10, hollow=True)
enemy_drop_area2 = Square(0, (WIN.height // 2) - card_height.value, card_width.value, card_height.value, COL.red.value, border_radius=10, hollow=True)
enemy_drop_area3 = Square(0, (WIN.height // 2) - card_height.value, card_width.value, card_height.value, COL.red.value, border_radius=10, hollow=True)


end_turn_image = Image()
end_turn_button = None

enemy_turn_image = Image().with_args(100 * 2, 100 * 2, 170 * 2, 150 * 2)

deck_image = Image().with_args(0, 0, card_width.value, card_height.value)
deck_image.place_bot(main.WIN)
deck_image.place_right(main.WIN)

deck_image.set_image(os.path.join("Assets", "Cards", "card_back.png"))

deck_image.x -= 100 * 2
deck_image.y -= 100 * 2

# energy_meter = Text(10, 10, COL.black.value, 60, "energy: 3")
# enemy_energy_meter = Text(10, 10, COL.black.value, 60, "ENEMY energy: 3")

card_combined_width = WIN.width * 0.2


def update_screen_size():

    global hand_cards, card_combined_width, enemy_cards

    new_size = pygame.Surface.get_size(WIN.win)

    WIN.width = new_size[0]
    WIN.height = new_size[1]

    card_combined_width = WIN.width * 0.2

    # os -> orinal size
    def update_size(object):
        object.width = object.original_size[0] / (1600 / WIN.width)
        object.height = object.original_size[1] / (900 / WIN.height)

    card_width.change((260 / 1.5) / (1600 / WIN.width))
    card_height.change((350 / 1.5) / (900 / WIN.height))

    for card in hand_cards + deck_cards + areas + enemy_areas + enemy_cards:
        # card.set_image(pygame.transform.scale(card.get_image(), (card_width, card_height)))
        card.resize(card_width.value, card_height.value)

    for object in [energy_meter, enemy_energy_meter, deck_image]:
        update_size(object)

    def update_position(object):
        

    hand_cards = align_x(card_combined_width, hand_cards)
    hand_cards = align_center_x(WIN.width, hand_cards)
    hand_cards = move_many("bot", hand_cards, WIN)

    enemy_cards = align_x(card_combined_width, enemy_cards)
    enemy_cards = align_center_x(WIN.width, enemy_cards)
    enemy_cards = move_many("top", enemy_cards, WIN)

    for card in active_cards:
        if card.value:
            card.value.resize(card_width.value, card_height.value)
            card.value.update_image()

    # background_image.width = WIN.width
    # background_image.height = WIN.height

    # background_image.update()

    background_image.resize(WIN.width, WIN.height)

class Energy_Meter(GameObject):
    def __init__(self, xPos, yPos, width, height, images):
        super().__init__(xPos, yPos, width, height)
        self.images = images
        self.image = None
        self.index = 3

        for image in self.images:
            image.x = self.x
            image.y = self.y
            image.width = self.width
            image.height = self.height

    def change(self, index):
        if index >= 0 and index <= 3:
            self.index = index
            self.image = self.images[index]
            self.image.update()

    def draw(self, window):

        for image in self.images:
            image.x = self.x
            image.y = self.y
            image.width = self.width
            image.height = self.height

        self.image.draw(window)

em_image0 = Image()
em_image1 = Image()
em_image2 = Image()
em_image3 = Image()

energy_meter = None
enemy_energy_meter = None

def set_ui():

    global energy_meter, enemy_energy_meter, end_turn_button

    os_end = ""

    match MAP_NAME.value:
        case "palace":
            os_end = "palace"
        case "planks":
            os_end = "planks"

    em_image0.set_image(os.path.join("Assets", "UI", os_end + "_energy_0.png"))
    em_image1.set_image(os.path.join("Assets", "UI", os_end + "_energy_1.png"))
    em_image2.set_image(os.path.join("Assets", "UI", os_end + "_energy_2.png"))
    em_image3.set_image(os.path.join("Assets", "UI", os_end + "_energy_3.png"))

    end_turn_image.set_image(os.path.join("Assets", "UI", os_end + "_end_turn.png"))
    enemy_turn_image.set_image(os.path.join("Assets", "UI", os_end + "_enemy_turn.png"))

    end_turn_button = Button.image_button(100 * 2, 100, 170 * 2, 150 * 2, event=END_TURN, image=end_turn_image)

    energy_meter = Energy_Meter(10 * 2, 10 * 2, 160 * 2, 150 * 2, (em_image0, em_image1, em_image2, em_image3))
    enemy_energy_meter = Energy_Meter(10 * 2, 10 * 2, 160 * 2, 150 * 2, (em_image0, em_image1, em_image2, em_image3))

    energy_meter.change(3)
    enemy_energy_meter.change(3)

    enemy_energy_meter.place_top_right(WIN)
    energy_meter.place_bot_left(WIN)

    energy_meter.x += 10
    energy_meter.y -= 10

    enemy_energy_meter.x -= 10
    enemy_energy_meter.y += 10

energy = 3
enemy_energy = 3

enemy_cards = [
    enemy_card1,
    enemy_card2,
    enemy_card3
]

areas = [
    drop_area1,
    drop_area2,
    drop_area3
]

enemy_areas = [
    enemy_drop_area1,
    enemy_drop_area2,
    enemy_drop_area3
]

for area in areas + enemy_areas:
    area.draw_text = False

active_card1,active_card2, active_card3 = Container(None), Container(None), Container(None)

enemy_active_card1, enemy_active_card2, enemy_active_card3 = Container(None), Container(None), Container(None)

active_cards = [
    active_card1,
    active_card2,
    active_card3
]

enemy_active_cards = [
    enemy_active_card1,
    enemy_active_card2,
    enemy_active_card3
]

areas = align_x(WIN.width * 0.5, areas)
areas = align_center_x(WIN.width, areas)

enemy_areas = align_x(WIN.width * 0.5, enemy_areas)
enemy_areas = align_center_x(WIN.width, enemy_areas)


hand_cards = align_x(card_combined_width, hand_cards)
enemy_cards = align_x(card_combined_width, enemy_cards)

hand_cards = align_center_x(WIN.width, hand_cards)
enemy_cards = align_center_x(WIN.width, enemy_cards)

hand_cards = move_bottom(WIN.height, hand_cards)
enemy_cards = move_top(enemy_cards)

hand_cards = set_original_positions(hand_cards)
hand_cards = set_hand_positions(hand_cards)

enemy_cards = set_original_positions(enemy_cards)
enemy_cards = set_hand_positions(enemy_cards)

is_own_turn = True
current_round = Container(1)

hand_cards = update_many_images(hand_cards)
deck_cards = update_many_images(deck_cards)
enemy_cards = update_many_images(enemy_cards)

def set_map(map):
    match map:
        case "planks":
            background_image.set_image(os.path.join("Assets", "Maps", "planks.jpg"))
        case "palace":
            background_image.set_image(os.path.join("Assets", "Maps", "palace.jpg"))


def load_scene(dt):

    DELTA_TIME = dt

    global cards, enemy_cards, enemy_active_card1, enemy_active_card2, enemy_active_card3, active_card1, active_card2, active_card3, hand_cards, deck_cards

    # print("1 ", enemy_active_card1)
    # print("2 ", enemy_active_card2)
    # print("3 ", enemy_active_card3)
    # print("own turn: ", is_own_turn)
    # print("enemy attacking: ", enemy_attacking)
    # print("active card 1:", active_card1)

    # print("active cards:")
    # print("1 ", active_card1.value)
    # print("2 ", active_card2.value)
    # print("3 ", active_card3.value)
    # print()

    # print("hand cards:")
    # for card in hand_cards:
    #     print(card)

    # print()

    if len(hand_cards) != 0 and hand_cards[0].get_animation() != None:
        print(hand_cards[0].get_animation().pct)
    

    # print(pygame.mouse.get_pos())


    # for i in range(len(hand_cards)):
    #     print(i + 1, "hovered: ", hand_cards[i].is_hovered, " position: ", hand_cards[i].x, hand_cards[i].y)
    # print()

    # print("FPS", 1 / dt)

    # print(card3.death_list)
    # print("round", current_round.value)

    clock = pygame.time.Clock()
    clock.tick(60)

    
        
    if is_own_turn:
        for card in hand_cards:
            card.is_draggable = True
        for container in active_cards:
            if container.value != None:
                container.value.is_draggable = True
    else:
        for card in hand_cards:
            card.is_draggable = False
        for container in active_cards:
            if container.value != None:
                container.value.is_draggable = False
    
    for card in enemy_cards:
        card.update_animation(DELTA_TIME)

    for card in active_cards:
        if card.value != None:
            card.value.update_animation(DELTA_TIME)

    for card in hand_cards:
        card.update_animation(DELTA_TIME)

    for card in enemy_cards + hand_cards:
        if card.health <= 0:
            card.lives -= 1
            card.health = 3
            card.current_state = 0

            if card == active_card1:
                active_card1.change(None)
            elif card == active_card2:
                active_card2.change(None)
            elif card == active_card3:
                active_card3.change(None)
            elif card == enemy_active_card1:
                enemy_active_card1.change(None)
            elif card == enemy_active_card2:
                enemy_active_card2.change(None)
            elif card == enemy_active_card3:
                enemy_active_card3.change(None)

            deck_cards.append(card)
        if card.lives <= 0:
            card.current_state = 2
            card.is_dead = True
            
    temp_list = []
    for card in hand_cards:
        if not card.is_dead:
            temp_list.append(card)
    hand_cards = temp_list.copy()

    temp_list = []
    for enemy_card in enemy_cards:
        if enemy_card.is_dead == False:
            temp_list.append(enemy_card)
    enemy_cards = temp_list.copy()

    if len(hand_cards) + len(deck_cards) == 0:
        pygame.event.post(pygame.event.Event(ENEMY_WON))

    if len(enemy_cards) == 0:
        pygame.event.post(pygame.event.Event(PLAYER_WON))


    # WIN.fill(COL.white.value)
    background_image.draw(WIN)

    if is_own_turn:
        WIN.draw_one(end_turn_button)
    else:
        WIN.draw_one(enemy_turn_image)

    WIN.draw_many(areas)
    WIN.draw_many(enemy_areas)
    WIN.draw_many(enemy_cards)
    WIN.draw_many(hand_cards)
    
    for card in active_cards:
        if card.value != None:
            WIN.draw_one(card.value)

    if len(deck_cards) >= 1:
        WIN.draw_one(deck_image)    

    # if energy_meter != None:

    if energy_meter.index != energy:
        energy_meter.change(energy)
    if enemy_energy_meter.index != enemy_energy:
        enemy_energy_meter.change(enemy_energy)

    WIN.draw_many((energy_meter, enemy_energy_meter))
    
# def drop_card():

#     for card in cards:

#         collision_count = 0
#         for area in areas:
#             if check_collision(card, area):
#                 collision_count = collision_count + 1
        
#         if collision_count <= 0 or collision_count > 1:
#             card.return_to_original_position()

enemy_attacking = False

def end_turn():
    global is_own_turn, energy
    
    # for card in cards, enemy_cards:
    #     if card.re_event != None:
    #         card.re_event()

    def set_hand_pos(obj, pos):
        obj.set_hand_pos(pos)
        obj.set_original_pos(pos)

    def add_card_to_hand(card_count):

        global hand_cards

        rand_card = deck_cards[random.randint(0, len(deck_cards) - 1)]
        
        rand_card.set_pos((deck_image.x, deck_image.y,))

        temp_card_list = []
        for i in range(len(hand_cards) + 1):
            temp_card_list.append(Square(0, 0, card_width, card_height, COL.black.value))

        

        hand_cards.append(rand_card)
        deck_cards.remove(rand_card)

        hand_cards = align_x(card_combined_width, hand_cards)
        hand_cards = align_center_x(WIN.width, hand_cards)
        hand_cards = move_bottom(WIN.height, hand_cards)

        # positions = get_x_centered_positions(WIN.width, get_x_aligned_positions(card_combined_width, temp_card_list))
        # positions = positions[len(positions) - 1]

        # target_pos = (positions.x, WIN.height - positions.height)
        target_pos = (rand_card.x, rand_card.y)
        rand_card.attach_animation(Animation(rand_card, (deck_image.x, deck_image.y), target_pos, Animation_Type.ease__in__out.value, 0.75, set_hand_pos, [rand_card, target_pos]))
        
        # rand_card.place_bot(WIN)

    if is_own_turn:
        is_own_turn = False

        energy = 3

        if len(hand_cards) < 3:
            add_card_to_hand(3 - len(hand_cards))
                

        def get_random_card():
            match random.randint(0, 2):
                case 0:
                    return enemy_card1
                case 1:
                    return enemy_card2
                case 2:
                    return enemy_card3
        
        def use_random_card():

            global enemy_attacking, is_own_turn

            temp_card = get_random_card()

            if active_card1.value == None and active_card2.value == None and active_card3.value == None:
                is_own_turn = True
                return None

            match random.randint(0, 2):
                case 0:
                    if active_card1.value != None and temp_card.current_state == 1:
                        enemy_attacking = True
                        attack(active_card1.value, temp_card)
                        
                    else: use_random_card()
                case 1:
                    if active_card2.value != None and temp_card.current_state == 1:
                        enemy_attacking = True
                        attack(active_card2.value, temp_card)

                    else: use_random_card()
                case 2:
                    if active_card3.value != None and temp_card.current_state == 1:
                        enemy_attacking = True
                        attack(active_card3.value, temp_card)
                        
                    else: use_random_card()
                        
                        

        def put_random_card():

            global enemy_active_card1, enemy_active_card2, enemy_active_card3, is_own_turn

            temp_card = get_random_card()

            match random.randint(0, 2):

                case 0:

                    if enemy_active_card1.value == None and temp_card.current_state == 0:
                        # temp_card.x = enemy_drop_area1.x
                        # temp_card.y = enemy_drop_area1.y

                        place(enemy_drop_area1, temp_card)

                        # temp_card.current_state = 1

                        enemy_active_card1.value = temp_card

                        # temp_card.set_original_pos((temp_card.x, temp_card.y))

                        # is_own_turn = True
                        
                        return True
                    else:
                        put_random_card()
                case 1:
                    
                    if enemy_active_card2.value == None and temp_card.current_state == 0:
                        # temp_card.x = enemy_drop_area2.x
                        # temp_card.y = enemy_drop_area2.y

                        place(enemy_drop_area2, temp_card)
                        enemy_active_card2.value = temp_card

                        # temp_card.current_state = 1

                        # temp_card.set_original_pos((temp_card.x, temp_card.y))

                        # is_own_turn = True
                        

                        return True
                    else:
                        put_random_card()
                case 2:
                    if enemy_active_card3.value == None and temp_card.current_state == 0:
                        # temp_card.x = enemy_drop_area3.x
                        # temp_card.y = enemy_drop_area3.y

                        place(enemy_drop_area3, temp_card)
                        enemy_active_card3.value = temp_card

                        # temp_card.current_state = 1

                        # temp_card.set_original_pos((temp_card.x, temp_card.y))

                        # is_own_turn = True
                        
                        return True
                    else:
                        put_random_card()

        def set_own_turn():
            global is_own_turn, enemy_attacking, enemy_energy
            is_own_turn = True
            enemy_attacking = False
            enemy_energy = 3
            

        def check_attack():
            if not enemy_energy <= 0:
                active_count = 0
                for card in enemy_cards:
                    if card.current_state == 1:
                        active_count += 1

                if active_count == len(enemy_cards):
                    use_random_card()
                elif active_count == 0:
                    put_random_card()
                else:
                    match random.randint(0, 1):
                        case 0:
                            use_random_card()
                        case 1:
                            put_random_card()
            else:
                set_own_turn()
                current_round.add_number(1)

        def attack_finished(attacker, victim):
            global enemy_energy
            victim.health -= attacker.damage
            enemy_energy -= attacker.cost
            attacker.attach_animation(Animation(attacker, (attacker.x, attacker.y), (attacker.get_original_pos()[0], attacker.get_original_pos()[1]), 4, 1, None))

            wait_and_call(1.5, check_attack)

        def set_op(card):
            print("NOGGER BLACK")
            card.set_original_pos((card.x, card.y))

        def place(area, card):
            card.current_state = 1
            card.attach_animation(Animation(card, (card.x, card.y), (area.x, area.y), Animation_Type.ease__in__out.value, 0.5, set_op, [card]))
            wait_and_call(2, check_attack)

        def attack(victim_card, attacker_card):
            attacker_card.attach_animation(Animation(attacker_card, (attacker_card.x, attacker_card.y), (victim_card.x, victim_card.y), 2, 0.5, attack_finished, (attacker_card, victim_card)))

        if not enemy_energy <= 0:
            active_count = 0
            for card in enemy_cards:
                if card.current_state == 1:
                    active_count += 1

            if active_count == len(enemy_cards):
                use_random_card()
            elif active_count == 0:
                put_random_card()
            else:
                match random.randint(0, 1):
                    case 0:
                        use_random_card()
                    case 1:
                        put_random_card()


                # use_random_card()

        
def drop_card(card):

    global active_card1, active_card2, active_card3, enemy_active_card1, enemy_active_card2, enemy_active_card3, energy

    match card.current_state:
        case 0:
            collision_count = 0
            for area in areas:
                if check_collision(card, area):
                    collision_count = collision_count + 1
                
            if collision_count <= 0 or collision_count > 1:
                card.return_to_original_position()
                return None

            if energy <= 0:
                return None

            for i in range(len(areas)):
                if check_collision(card, areas[i]):
                    if active_cards[i].value == None:
                        active_cards[i].value = card
                        hand_cards.remove(card)

                        card.x = areas[i].x
                        card.y = areas[i].y
                        card.set_original_pos((card.x, card.y))

                        card.current_state = 1

                        energy -= 1
                    else:
                        card.return_to_original_position()
                        


            # if check_collision(card, drop_area1):
            #     if active_card1.value == None:
            #         active_card1.value = card

            #         card.x = drop_area1.x
            #         card.y = drop_area1.y
            #         card.set_original_pos((card.x, card.y))

            #         card.current_state = 1

            #         energy -= 1

            #         # card.is_draggable = False
            #     else:
            #         card.return_to_original_position()
            # elif check_collision(card, drop_area2):
            #     if active_card2.value == None:
            #         active_card2.value = card

            #         card.x = drop_area2.x
            #         card.y = drop_area2.y

            #         card.set_original_pos((card.x, card.y))

            #         card.current_state = 1

            #         energy -= 1

            #         # card.is_draggable = False
            #     else:
            #         card.return_to_original_position()
            # elif check_collision(card, drop_area3):
            #     if active_card3.value == None:
            #         active_card3.value = card

            #         card.x = drop_area3.x
            #         card.y = drop_area3.y

            #         card.set_original_pos((card.x, card.y))

            #         card.current_state = 1

            #         energy -= 1

            #         # card.is_draggable = False
            #     else:
            #         card.return_to_original_position()
        case 1:

            collision_count = 0

            if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                for area in enemy_areas:
                    if check_collision(card, area):
                        collision_count = collision_count + 1

            if card.range == attackable.own_cards.value or card.range == attackable.all_cards.value:
                for area in areas:
                    if check_collision(card, area):
                        collision_count = collision_count + 1
                

            if collision_count <= 0 or collision_count > 1:
                card.return_to_original_position()
                return None

            if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                if check_collision(card, enemy_drop_area1):
                    if enemy_active_card1.value != None:
                        # enemy_active_card1.current_state = 0
                        # enemy_active_card1.return_to_original_position()

                        # enemy_active_card1 = None

                        if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                            enemy_active_card1.value.health -= card.damage
                            if card.effect != None:
                                card.effect(card, enemy_active_card1.value)
                            energy -= card.cost

                    card.return_to_original_position()
                elif check_collision(card, enemy_drop_area2):
                    if enemy_active_card2.value != None:
                        # enemy_active_card2.current_state = 0
                        # enemy_active_card2.return_to_original_position()

                        # enemy_active_card2 = None

                        if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                            enemy_active_card2.value.health -= card.damage
                            if card.effect != None:
                                card.effect(card, enemy_active_card2.value)
                            energy -= card.cost

                    card.return_to_original_position()
                elif check_collision(card, enemy_drop_area3):
                    if enemy_active_card3 != None:
                        # enemy_active_card3.current_state = 0
                        # enemy_active_card3.return_to_original_position()

                        # enemy_active_card3 = None
                        if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                            enemy_active_card3.value.health -= card.damage
                            if card.effect != None:
                                card.effect(card, enemy_active_card3.value)
                            energy -= card.cost

                    card.return_to_original_position()
                
                
            # checking own zones for blue cards
            if card.range == attackable.own_cards.value or card.range == attackable.all_cards.value:
                if check_collision(card, drop_area1):
                    if active_card1.value != None and active_card1.value != card:
                        if card.range == attackable.own_cards.value:
                            card.effect(card, active_card1.value)
                            energy -= card.cost
                    card.return_to_original_position()

                elif check_collision(card, drop_area2):
                    if active_card2.value != None and active_card2.value != card:
                        if card.range == attackable.own_cards.value:
                            card.effect(card, active_card2.value)
                            energy -= card.cost
                    card.return_to_original_position()

                elif check_collision(card, drop_area1):
                    if active_card3.value != None and active_card3.value != card:
                        if card.range == attackable.own_cards.value:
                            card.effect(card, active_card3.value)
                            energy -= card.cost
                    card.return_to_original_position()

                else:
                    card.return_to_original_position()

    
            
            

    

# game_scene = pygpp.Scene()

