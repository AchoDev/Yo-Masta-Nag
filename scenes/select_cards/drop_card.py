from cls import *


def check_drop(object):
    for area in drop_areas:
        if Window.get_rect(area).colliderect(Window.get_rect(object)):
            object.set_transform(area)
            return None
    
    object.set_transform(Transform(
        object.original_pos[0],
        object.original_pos[1],

        object.original_size[0],
        object.original_size[1]
    ))



class Drop_Area(GameObject):
    def __init__(self, xPos, yPos, index):
        super().__init__(xPos, yPos, 300, 400)
        self.put_card = None
        self.color = COL.white.value

        self.index = index

    def place_card(self, card):
        self.put_card = card

    def draw(self, window):
        Square(self.x, self.y, self.width, self.height, self.color, 1, True).draw(window)


        
    
drop_areas = [
    Drop_Area(1000, 600, 0),
    Drop_Area(1000, 600, 1),
    Drop_Area(1000, 600, 2),
    Drop_Area(1000, 600, 3),
    Drop_Area(1000, 600, 4),
]

align_grid(drop_areas, 1000, 1000, 3)

