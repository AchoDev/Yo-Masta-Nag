import pygame, cls, delta_time, console
from .obj import reset_board

CARD_DROP = pygame.USEREVENT + 2
END_TURN = pygame.USEREVENT + 3

PLAYER_WON = pygame.USEREVENT + 4
ENEMY_WON = pygame.USEREVENT + 5

game_running = True

def start_game():

    reset_board()
    while True:
        delta_time.update_delta_time()

        for event in pygame.event.get():
            if event.type == END_TURN:
                cls.end_turn()
            if event.type == PLAYER_WON:
                console.log("player won")
            if event.type == ENEMY_WON:
                console.log("enemy_won")