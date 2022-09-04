
import math, threading, time, copy
from cls.Window import Window

def align_x(x_space, objects):
    i = 1
    ln = len(objects)
    for object in objects:
        object.x = ((x_space // ln) * i) - ( ( (x_space // ln) // 2) + (object.width // 2))
        i = i + 1

def get_x_aligned_positions(x_space, objects):
    unref_objs = copy.copy(objects) 
    unref_objs = align_x(x_space, objects)
    list = []
    # for obj in unref_objs:
    #     list.append(obj.x)
    # return list
    return unref_objs

def get_x_centered_positions(window_width, objects):
    unref_objs = copy.copy(objects)
    unref_objs = align_center_x(window_width, objects)
    list = []
    # for obj in unref_obj:
    #     list.append(obj.x)
    return unref_objs

def align_y(y_space, objects):
    i = 1
    ln = len(objects)
    for object in objects:
        object.y = ((y_space // ln) * i) - ( ( (y_space // ln) // 2) + (object.height // 2))
        i = i + 1

def move_bottom(height, objects):
    for object in objects:
        object.y = height - object.height
    return objects

def move_top(objects):
    for object in objects:
        object.y = 0
    return objects

def align_center_x(window_width, objects):

    middle_point = 0

    for object in objects:
        middle_point = middle_point + (object.x + (object.width // 2))

    middle_point = middle_point // len(objects)

    for object in objects:
        object.x = object.x + (window_width // 2 - middle_point)

    return objects
    
def align_center_y(window_height, objects):

    middle_point = 0

    for object in objects:
        middle_point = middle_point + (object.y + (object.height // 2))

    middle_point = middle_point // len(objects)

    for object in objects:
        object.y = object.y + (window_height // 2 - middle_point)

    return objects

def set_original_positions(objects):
    for object in objects:
        object.set_original_pos((object.x, object.y))

    return objects
    
def set_hand_positions(objects):
    for object in objects:
        object.set_hand_pos((object.x, object.y))
    return objects

def check_collision(object_1, object_2):
    if Window.get_rect(object_1).colliderect(Window.get_rect(object_2)): return True
    return False

def sync_transform(object_1, object_2):
    object_2.x = object_1.x
    object_2.y = object_1.y

    object_2.width = object_1.width
    object_2.height = object_1.height

def sync_position(target, changed_obj):
    changed_obj.x = target.x
    changed_obj.y = target.y

def update_many_images(objects):
    for object in objects:
        object.update_image()

    return objects 

def align_grid_center(objects, width, height, window, colums):
    big_list = []

    for i in range(math.ceil(len(objects) / colums)):
        small_list = []
        for j in range(colums):
            if j + (i * colums) >= len(objects): break
            small_list.append(objects[j + (i * colums)])

        big_list.append(small_list)


    for list in big_list:
        align_x(width, list)
        align_center_x(window.width, list)

    for i in range(len(big_list[0])):
        temp_list = []
        for j in range(len(big_list)):
            try:
                temp_list.append(big_list[j][i])
            except:
                pass

        align_y(height, temp_list)
        align_center_y(window.height, temp_list)
        

# def wait_and_call(time, function):

#     async def head():
#         t = asyncio.create_task(wait_for_seconds())
#         await t

#     async def wait_for_seconds():
#         await asyncio.sleep(time)
#         print("negos")
#         function()
    
#     asyncio.run(head())

#     print("END")

def wait_and_call(sec, function):
    def wait_for_seconds():
        time.sleep(sec)
        function()
    
    threading.Thread(target=wait_for_seconds).start()
    
def move_many(direction, objects, win):
    for object in objects:
        match direction:
            case "top":
                object.place_top()
            case "right":
                object.place_right(win)
            case "bot":
                object.place_bot(win)
            case "left":
                object.place_left()
            
