#基础知识for循环
from datetime import datetime

import time

import random


odds=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
for i in range(5):
    right_this_minute=datetime.today().minute

    if right_this_minute in odds:
        print("this minute seems in odds")
    else:
        print("this minute seems not in odds!")
    wait_time=random.randint(1,60)
    time.sleep(wait_time)

