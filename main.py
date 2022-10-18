
import os, sys, pygame
from cls.Window import Window

pygame.init()

info = pygame.display.Info()

SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
print(pygame.display.list_modes(32))
print(pygame.display.mode_ok((1680, 1050), 0, 32))
 

# WIN = Window(1920 / 1, 1080 / 1)
# WIN = Window(2560, 1600)
WIN = Window(1340, 900)

CANVAS_SIZE = (1920, 1080)

from scenes.select_cards import scene as select_cards
import cls

# 1300
# 800
# 1440, 900
# 2560, 1600


FPS = 60


def init():

    START_EVENT = pygame.USEREVENT + 67
    CARD_EVENT = pygame.USEREVENT + 68
    

    button_width, button_height = 200 * 2, 50 * 2
    start_button = cls.Button(WIN.get_center()[0] - button_width // 2, WIN.get_center()[1] - button_height // 2, 50, button_width, button_height, cls.COL.blue.value, "start", START_EVENT)
    card_button = cls.Button(WIN.get_center()[0] - button_width // 2, (WIN.get_center()[1] - button_height // 2) + 70, 50, button_width, button_height, cls.COL.blue.value, "cards", CARD_EVENT)
    option_button = cls.Button(WIN.get_center()[0] - button_width // 2, (WIN.get_center()[1] - button_height // 2) + 140, 50, button_width, button_height, cls.COL.blue.value, "option",  START_EVENT)
    exit_button = cls.Button(WIN.get_center()[0] - button_width // 2, (WIN.get_center()[1] - button_height // 2) + 210, 50, button_width, button_height, cls.COL.blue.value, "exit", START_EVENT)

    buttons = [
        start_button,
        card_button,
        option_button,
        exit_button
    ]

    menu_text = cls.Text(0, 100, 100, cls.COL.blue.value, "yo masta NAG !!")
    menu_text.set_x(WIN.get_center()[0] - menu_text.get_width() // 2)

    # currentScene = "logo"
    currentScene = "menu"

    run = True

    clock = pygame.time.Clock()
    start = False

    current_drawn = []
        
    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == START_EVENT:
                start = True
                currentScene = "select_map"
                select_cards.load_scene()
            if event.type == CARD_EVENT:
                currentScene = "card_list"
            # if event.type == CARD_DROP:
            #     # game.drop_card()
            #     pass
            
            
            # if event.type == sm.SELECT_PLANKS:
            #     # game.MAP_NAME.change("planks")
            #     # game.set_map("planks")
            #     # game.set_ui()
            #     currentScene = "select_cards"
            # if event.type == sm.SELECT_PALACE:
            #     # game.MAP_NAME.change("palace")
            #     # game.set_map("palace") #! UUPDATE THIS HERE
            #     # game.set_ui()
            #     currentScene = "select_cards"
            # if event.type == cl.RETURN_TO_MENU:
            #     currentScene = "menu"

            # if event.type == cs.START_GAME_EVENT:
            #     currentScene = "game"

            # if event.type == cl.CARD_LIST_LEFT_PRESS:
            #     cl.page_index.add_number(-1)
            # if event.type == cl.CARD_LIST_RIGHT_PRESS:
            #     cl.page_index.add_number(1)
            
            if event.type == pygame.VIDEORESIZE:
                if currentScene == "game":
                    pass
                    # game.update_screen_size()


        WIN.fill(cls.COL.white.value)
        menu_text.draw(WIN)

        for button in buttons:
            button.draw(WIN)
        # match currentScene:
        #     case "menu":
        #         WIN.fill(COL.yellow.value)
                
        #         # if start:
        #         #     currentScene = "game"
                
        #         menu_text.draw(WIN)

        #         for button in buttons:
        #             button.draw(WIN)
        #     case "game":
        #         # game.load_scene(DELTA_TIME)
        #         load_game_scene()

        #     case "player_win":
        #         win_screen.load_scene("player")
        #     case "enemy_win":
        #         win_screen.load_scene("enemy")
        #     case "select_map":
        #         sm.load_scene()
        #     case "card_list":
        #         cl.load_scene()
        #     case "select_cards":
        #         cs.load_scene()



        pygame.display.update()

if __name__ == "__main__":
    init()