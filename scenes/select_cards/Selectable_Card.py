from cls import *
from .drop_card import check_drop

class Selectable_Card(GameObject, Draggable):
    def __init__(self, xPos, yPos, width, height, image):
        GameObject.__init__(self, xPos, yPos, width, height)
        Draggable.__init__(self)

        self.original_pos = (self.x, self.y)
        self.original_size = (self.width, self.height)

        self.image = image

    def drop(self):
        check_drop(self)
            
    def update(self):
        self.drag()

    def draw(self, window):
        # Draggable.draw(Selectable_Card, self) 
        sync_transform(self, self.image)


        window.draw_one(Square(*self.original_pos, *self.original_size, COL.white.value, hollow=True), 1920)

        self.image.resize(self.width, self.height)
        self.image.draw(window)

        



