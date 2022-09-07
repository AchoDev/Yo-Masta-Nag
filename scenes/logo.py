
import os
from cls.Button import Button
import main
import pygame


from cls.Image import Image
from cls.Colors import COL

logo = Image().with_args(0, 0, 200, 200)
# logo.set_image(os.path.join())

def load_scene():
    main.WIN.fill(COL.yellow.value)

    