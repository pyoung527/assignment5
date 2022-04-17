'''
COMP-216 SEC.004 W22 
Assignment5
Group 7
@author = [
    Young Park,
        ]    
'''
import time
import numpy as np


def generator():

    start_time = time.time()
    interval = 2

    while True:
        current_time = time.time()
        elapsed = current_time - start_time

        if elapsed > interval:

            x = np.linspace(0, 100, num=1000)
            noise = np.random.normal(scale=5, size=len(x))
            y = 100*(np.sin(x/10*np.pi)) + noise

            data = {
                'timestamp': current_time,
                'x': x,
                'y': y
            }

            return data
