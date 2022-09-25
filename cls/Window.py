
from curses import window
import pygame, copy, sys
from .Transform import Transform
from .Container import Container
from .Square import Square
from .Colors import COL
from .Text import Text

sys.path.append("..")

from delta_time import average_fps

window_ratio = Container(0)

debug_mode = Container(False)
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE, 32)

    def draw_many(self, objects, canvas_width, prn=False):
        for object in objects:
            # self.win.blit(object.get_body(), (object.x, object.y))
            self.draw_one(object, canvas_width, prn) 

    def draw_one(self, obj, canvas_width, prn=False):


        window_ratio.change(self.width / canvas_width)
        ratio = window_ratio.value # l + ratio
        
        if type(obj).__name__ == "Text":
            original_font_size = obj.font_size
            obj.font_size = int(obj.font_size * ratio)             
        
            
        obj.update()

        ot = Transform(obj.x, obj.y, obj.width, obj.height) # ot -> original transform

        obj.x *= ratio
        obj.y *= ratio
        
        obj.width *= ratio
        obj.height *= ratio

        obj.draw(self)

        if prn and debug_mode.value:
            # print(obj.width)
            # print(obj.height)
            self.draw_rect(Square(ot.x, ot.y, ot.width, ot.height, COL.blue.value, hollow=True), COL.green.value)

        obj.set_transform(ot)

        if type(obj).__name__ == "Text":
            obj.font_size = original_font_size

        
        if debug_mode.value:
            abs_m_pos = pygame.mouse.get_pos()
            rel_m_pos = (pygame.mouse.get_pos()[0] // window_ratio.value, pygame.mouse.get_pos()[1] // window_ratio.value)

            self.draw_rect(Square(abs_m_pos[0] - 10, abs_m_pos[1] - 10, 20, 20, COL.red.value), COL.red.value)
            self.draw_rect(Square(rel_m_pos[0] - 10, rel_m_pos[1] - 10, 20, 20, COL.red.value), COL.violet.value)

    def draw_rect(self, obj, color):
        rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
        pygame.draw.rect(self.win, color, rect, 2 if obj.is_hollow else 0 ,border_radius=obj.border_radius)

    def draw_transparent_square(self, obj, color, alpha):
        s = pygame.Surface((obj.x * window_ratio.value, obj.y * window_ratio.value))
        s.set_alpha(alpha)                
        s.fill(color)           
        self.win.blit(s, (obj.x * window_ratio.value, obj.y * window_ratio.value))

    def draw_line(self, obj, color):
        pygame.draw.line(self.win, color, (obj.x1, obj.y1), (obj.x2, obj.y2), 1)

    def get_rect(self, object):
        return pygame.Rect(object.x, object.y, object.width, object.height)

    def fill(self, color):
        self.win.fill(color)
    
    def get_center(self):
        return [self.width // 2, self.height // 2]

    def videoresize(self):
        self.width = self.win.get_width()
        self.height = self.win.get_height()

    @staticmethod
    def get_rect(object):
        return pygame.Rect(object.x, object.y, object.width, object.height)