import time
from cls.Container import Container

DELTA_TIME = 0
prev_time = time.time()

def update_delta_time():
    now = time.time()
    DELTA_TIME = now - prev_time
    prev_time = now