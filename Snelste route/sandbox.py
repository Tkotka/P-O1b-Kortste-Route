import time

from PIL.DdsImagePlugin import item1

from Optimalisatie_startfile3 import *

import math
counter = 1
while True:
    t1 = time.perf_counter()
    time.sleep(0.1)
    t2 = time.perf_counter()
    diff = t2-t1
    if counter == 1:
        avg = diff
    else:
        if avg is None:
            avg = 0.1
        avg = ((counter-1)*avg + diff)/counter
    if counter % 10 == 0:
        print(avg)
    counter += 1