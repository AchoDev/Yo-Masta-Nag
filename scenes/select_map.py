import main, sys, os, pygame

sys.path.append("..")

from cls.Button import Button
from cls.Image import Image
from cls.Colors import COL
from cls.Text import Text

SELECT_PLANKS = pygame.USEREVENT + 10
SELECT_PALACE = pygame.USEREVENT + 11

planks_image = Image()
planks_image.set_image(os.path.join("Assets", "Maps", "planks.jpg"))

planks_button = Button.image_button(100, 100, 300, 200, SELECT_PLANKS, planks_image)


palace_image = Image()
palace_image.set_image(os.path.join("Assets", "Maps", "palace.jpg"))

palace_button = Button.image_button(500, 100, 300, 200, SELECT_PALACE, palace_image)

head_text = Text(200, 10, COL.black.value, 120, "SEELECr MAp")

def load_scene():
    main.WIN.fill(COL.yellow.value)

    planks_button.draw(main.WIN)
    palace_button.draw(main.WIN)

    head_text.draw(main.WIN)