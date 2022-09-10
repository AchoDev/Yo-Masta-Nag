
import pygame, copy

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE, 32)

    def draw_many(self, objects):
        for object in objects.copy():
            # self.win.blit(object.get_body(), (object.x, object.y))
            self.draw_one(object)

    def draw_one(self, object):

        obj = copy.copy(object)
        ratio = object.width / self.width # l + ratio
            
        obj.x /= ratio
        obj.y /= ratio
        
        obj.width /= ratio
        obj.height /= ratio

        obj.draw(self)

    def draw_rect(self, obj, color):
        rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
        pygame.draw.rect(self.win, color, rect, 2 if obj.is_hollow else 0 ,border_radius=obj.border_radius)

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