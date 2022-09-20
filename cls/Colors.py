
import enum

class COL(enum.Enum):
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    violet = (204, 153, 255)

    def __repr__(self):
        return self.value