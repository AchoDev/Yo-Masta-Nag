class GameObject:
    def __init__(self, xPos, yPos, width = 0, height = 0, zLayer = 0):
        self.x = xPos
        self.y = yPos
        self.layer = zLayer
        self.width = width
        self.height = height

        self.__animation = None

        self.original_size = [width, height]

    def attach_animation(self, animation):
        self.__animation = animation

    def resize(self, width, height):
        self.width = width
        self.height = height

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_animation(self):
        return self.__animation

    def update_animation(self, dt):
        if self.__animation != None:
            if self.__animation.is_finished == True:
                    self.__animation = None
            else:
                self.__animation.update(dt)
            return True
        else:
            return False

    def place_center(self, win):
        self.x = win.get_center()[0] - self.get_width() // 2
        self.y = win.get_center()[1] - self.get_height() // 2

    def place_right(self, win):
        self.x = win.width - self.width
    
    def place_left(self):
        self.x = 0

    def place_top(self):
        self.y = 0

    def place_bot(self, win):
        self.y = win.height - self.height

    def place_top_right(self, win):
        self.place_right(win)
        self.place_top()

    def place_bot_left(self, win):
        self.place_left()
        self.place_bot(win)
