import time
from cls.Container import Container

DELTA_TIME = 0
prev_time = time.time()

count = 30
__fps_list = []
average_fps = 0

def update_delta_time():
    global prev_time, DELTA_TIME
    now = time.time()
    DELTA_TIME = now - prev_time
    prev_time = now

    __fps_list.append(get_fps())

    if len(__fps_list) == count:
        print(get_average_fps())
        __fps_list.clear()


def get_fps():
    return 0 if DELTA_TIME == 0 else 1 / DELTA_TIME

def get_average_fps():
    fps = 0

    for num in __fps_list:
        fps += num

    fps /= len(__fps_list)

    return fps