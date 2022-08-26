
import pygame

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE, 32)

    def draw_many(self, objects):
        for object in objects:
            # self.win.blit(object.get_body(), (object.x, object.y))
            object.draw(self)

    def draw_one(self, object):
        object.draw(self)

    def draw_rect(self, obj, color):
        rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
        pygame.draw.rect(self.win, color, rect, 2 if obj.is_hollow else 0 ,border_radius=obj.border_radius)

    def get_rect(self, object):
        return pygame.Rect(object.x, object.y, object.width, object.height)

    def fill(self, color):
        self.win.fill(color)
    
    def get_center(self):
        return [self.width // 2, self.height // 2]

    @staticmethod
    def get_rect(object):
        return pygame.Rect(object.x, object.y, object.width, object.height)