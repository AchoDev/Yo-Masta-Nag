

from .obj import *
from main import WIN, CANVAS_SIZE
import cls, copy

def draw_scene():
    WIN.fill(cls.COL.white.value)

    # background_copy = copy.copy(background)

    # background_copy.width /= background.width / WIN.width
    # background_copy.height /= background.width / WIN.width

    # print(f"{background.width} / {WIN.width} = {background.width / WIN.width}")
    # print(f"bg width: {background_copy.width}")
    # print(f"bg height: {background_copy.height}")

    WIN.draw_one(background, 1920)
    WIN.draw_one(left_button, 1920)

    WIN.draw_many([cards_background_border, cards_background], 1920)
    WIN.draw_many([left_button, right_button, head_text, page_text], 1920)
