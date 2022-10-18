
import pygame, cls, delta_time, console
from .obj import *
from .draw import load_game_scene

CARD_DROP = pygame.USEREVENT + 2
END_TURN = pygame.USEREVENT + 3

PLAYER_WON = pygame.USEREVENT + 4
ENEMY_WON = pygame.USEREVENT + 5

game_running = True

def start_game(cards):

    reset_board(cards)
    while True:



        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:

                    if console.is_visible:
                        console.is_visible = False
                    else:
                        console.is_visible = True

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == END_TURN:
                cls.end_turn()
            if event.type == PLAYER_WON:
                console.log("player won")
            if event.type == ENEMY_WON:
                console.log("enemy_won")

        load_game_scene()        

        console.draw_console()
        delta_time.update_delta_time()

        pygame.display.update()
