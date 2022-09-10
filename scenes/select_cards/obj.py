
from main import CANVAS_SIZE as cs
import pygame, sys

sys.path.append("..")
sys.path.append("..")
sys.path.append(".")

from cls import *

background = Square(0, 0, 1920, 1080, COL.blue.value)

head_text = Text(0, 0, 120, COL.black.value, "SELECT CARDS")

page_text = Text(100, 0, 50, COL.black.value, "Page 999/6")

LEFT_BUTTON_PRESS = pygame.USEREVENT + 20
RIGHT_BUTTON_PRESS = pygame.USEREVENT + 21

left_button = Button(0, 200, 70, 70, COL.white.value, "<", LEFT_BUTTON_PRESS, 1)
right_button = Button(300, 0, 70, 70, COL.white.value, ">", RIGHT_BUTTON_PRESS, 1)

left_button.place_left()
right_button.place_right(cs[0])

cb_y = 100
cb_height = 400
cb_border_width = 5

left_button.y = cb_y + cb_height // 2 - left_button.height // 2
right_button.y = cb_y + cb_height // 2 - right_button.height // 2

cards_background = Square(0, cb_y, cs[0], cb_height, COL.yellow.value)
cards_background_border = Square(-10, cb_y - cb_border_width, cs[0], cb_height + cb_border_width * 2, COL.black.value)