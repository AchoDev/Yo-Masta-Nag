import pygame, sys
import cls

sys.path.append("..")
sys.path.append("..")

import delta_time
import scenes

CARD_DROP = pygame.USEREVENT + 2
END_TURN = pygame.USEREVENT + 3

PLAYER_WON = pygame.USEREVENT + 4
ENEMY_WON = pygame.USEREVENT + 5

game_running = True

def start_game():

    cls.obj.reset_board()
    while game_running:
        delta_time.update_delta_time()

        for event in pygame.event.get():
            if event.type == END_TURN:
                cls.end_turn()
            if event.type == PLAYER_WON:
                scenes.scene_manager.load_scene("win_screen", ["player"])
            if event.type == ENEMY_WON:
                scenes.scene_manager.load_scene("win_screen", ["enemy"])