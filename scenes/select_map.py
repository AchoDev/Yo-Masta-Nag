
import os, pygame
import re
from main import WIN
import cls
from scenes.game_src.draw import load_game_scene
from scenes.game_src.obj import reset_board

SELECT_PLANKS = pygame.USEREVENT + 10
SELECT_PALACE = pygame.USEREVENT + 11

planks_image = cls.Image()
planks_image.set_image(os.path.join("Assets", "Maps", "planks.jpg"))

planks_button = cls.Button.image_button(100, 100, 300, 200, SELECT_PLANKS, planks_image)


palace_image = cls.Image()
palace_image.set_image(os.path.join("Assets", "Maps", "palace.jpg"))

palace_button = cls.Button.image_button(500, 100, 300, 200, SELECT_PALACE, palace_image)

head_text = cls.Text(200, 10, cls.COL.black.value, 120, "SEELECr MAp")

def load_scene():
    while(True):
        for event in pygame.event.get():
            if event.type == SELECT_PALACE:
                reset_board()
                load_game_scene()
            if event.type == pygame.QUIT:
                pygame.quit()

        WIN.fill(cls.COL.yellow.value)

        planks_button.draw(WIN)
        palace_button.draw(WIN)

        head_text.draw(WIN)

        pygame.display.update()