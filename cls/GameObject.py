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

    def set_transform(self, transform):
        self.x = transform.x
        self.y = transform.y
        self.width = transform.width
        self.height = transform.height

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

    def update(self):
        pass

    def place_center(self, width, height):
        self.x = width // 2 - self.width // 2
        self.y = height // 2 - self.height // 2

    def place_right(self, width):
        self.x = width - self.width
    
    def place_left(self):
        self.x = 0

    def place_top(self):
        self.y = 0

    def place_bot(self, height):
        self.y = height - self.height

    def place_top_right(self, width):
        self.place_right(width)
        self.place_top()

    def place_bot_left(self, height):
        self.place_left()
        self.place_bot(height)

    def place_bot_right(self, width, height):
        self.place_right(width)
        self.place_bot(height)

    def place_center_left(self, height):
        self.x = 0
        self.y = height // 2 - self.height // 2

    def place_center_right(self, width, height):
        self.x = width - self.width
        self.y = height // 2 - self.height // 2
