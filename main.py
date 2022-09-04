
import os, sys, pygame
from cls.Window import Window

pygame.init()

info = pygame.display.Info()

SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
print(pygame.display.list_modes(32))
print(pygame.display.mode_ok((1680, 1050), 0, 32))


# WIN = Window(1920 / 1, 1080 / 1)
# WIN = Window(2560, 1600)
WIN = Window(1440, 900)

import time, scenes.win_screen as win_screen, scenes.select_map as sm, scenes.card_list as cl, scenes.card_select as cs
from scenes.game_src.all import *
# from cls import GameObject, Image, Scene, Window, COL, Button, Text

from cls.Button import Button
from cls.Card import Card
from cls.Colors import COL
from cls.functions import *
from cls.GameObject import GameObject
from cls.Point import Point
from cls.Text import Text
from cls.Container import Container

# 1300
# 800
# 1440, 900
# 2560, 1600


FPS = 60


def init():

    START_EVENT = pygame.USEREVENT + 1
    CARD_EVENT = pygame.USEREVENT + 6
    

    button_width, button_height = 200 * 2, 50 * 2
    start_button = Button(WIN.get_center()[0] - button_width // 2, WIN.get_center()[1] - button_height // 2, button_width, button_height, COL.white.value, "start", 50, START_EVENT)
    card_button = Button(WIN.get_center()[0] - button_width // 2, (WIN.get_center()[1] - button_height // 2) + 70, button_width, button_height, COL.white.value, "cards", 50, CARD_EVENT)
    option_button = Button(WIN.get_center()[0] - button_width // 2, (WIN.get_center()[1] - button_height // 2) + 140, button_width, button_height, COL.white.value, "option", 50, START_EVENT)
    exit_button = Button(WIN.get_center()[0] - button_width // 2, (WIN.get_center()[1] - button_height // 2) + 210, button_width, button_height, COL.white.value, "exit", 50, START_EVENT)

    buttons = [
        start_button,
        card_button,
        option_button,
        exit_button
    ]

    menu_text = Text(0, 100, COL.blue.value, 100, "yo masta NAG !!")
    menu_text.set_x(WIN.get_center()[0] - menu_text.get_width() // 2)

    # currentScene = "logo"
    currentScene = "menu"

    run = True

    clock = pygame.time.Clock()
    start = False

    current_drawn = []

    

    def load_scene(scene):
        scene.load()
        
    while run:

        clock.tick(FPS)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == START_EVENT:
                start = True
                currentScene = "select_map"
            if event.type == CARD_EVENT:
                currentScene = "card_list"
            if event.type == CARD_DROP:
                # game.drop_card()
                pass
            
            
            if event.type == sm.SELECT_PLANKS:
                # game.MAP_NAME.change("planks")
                # game.set_map("planks")
                # game.set_ui()
                currentScene = "select_cards"
            if event.type == sm.SELECT_PALACE:
                # game.MAP_NAME.change("palace")
                # game.set_map("palace") #! UUPDATE THIS HERE
                # game.set_ui()
                currentScene = "select_cards"
            if event.type == cl.RETURN_TO_MENU:
                currentScene = "menu"

            if event.type == cs.START_GAME_EVENT:
                currentScene = "game"

            if event.type == cl.CARD_LIST_LEFT_PRESS:
                cl.page_index.add_number(-1)
            if event.type == cl.CARD_LIST_RIGHT_PRESS:
                cl.page_index.add_number(1)
            
            if event.type == pygame.VIDEORESIZE:
                if currentScene == "game":
                    pass
                    # game.update_screen_size()



        match currentScene:
            case "menu":
                WIN.fill(COL.yellow.value)
                
                # if start:
                #     currentScene = "game"
                
                menu_text.draw(WIN)

                for button in buttons:
                    button.draw(WIN)
            case "game":
                # game.load_scene(DELTA_TIME)
                load_game_scene()

            case "player_win":
                win_screen.load_scene("player")
            case "enemy_win":
                win_screen.load_scene("enemy")
            case "select_map":
                sm.load_scene()
            case "card_list":
                cl.load_scene()
            case "select_cards":
                cs.load_scene()



        pygame.display.update()

if __name__ == "__main__":
    init()