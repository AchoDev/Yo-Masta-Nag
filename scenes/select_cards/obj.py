
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

left_button = Button(0, 200, 50, 50, COL.black.value, "<", LEFT_BUTTON_PRESS, 1)
right_button = Button(300, 0, 50, 50, COL.black.value, ">", RIGHT_BUTTON_PRESS, 1)