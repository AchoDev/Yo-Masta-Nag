import pygame
from .Colors import COL
from .Text import Text
from .GameObject import GameObject
from .functions import sync_position, sync_transform




class Button(GameObject):
    def __init__(self, xPos=0, yPos=0, width=100, height=35, 
                color=COL.white, text="text", event=None, 
                border_radius=0, hollow=False):

        super().__init__(xPos, yPos, width, height)


        self.color = color

        if text != "IMAGE_BUTTON":
            self.text = Text(self.x, self.y, width // 10, COL.black.value, text)
        
        self.event = event

        self.border_radius = border_radius
        self.is_hollow = hollow

        self.clicked = False

        self.__image = None


    def set_image(self, image):
        self.__image = image

    @classmethod
    def image_button(cls, xPos, yPos, width, height, event, image):
        btn = cls(xPos, yPos, width, height, None, "IMAGE_BUTTON", None, event)
        btn.set_image(image)
        btn.update_image()

        return btn

    def update_image(self):
        sync_transform(self, self.__image)
        self.__image.update()


    def draw(self, window):

        if self.__image == None:
            window.draw_rect(self, self.color)
            sync_position(self, self.text)
            self.text.draw(window)
        else:
            self.__image.draw(window)
        
        m_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] == 1:

            if self.clicked == False:
                if window.get_rect(self).collidepoint(m_pos):

                    # print(m_pos, self.x, self.y, self.width, self.height)
                    # print(window.get_rect(self).collidepoint(m_pos))

                    self.clicked = True
                    pygame.event.post(pygame.event.Event(self.event))
                    

        elif pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = False