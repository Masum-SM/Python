"""  
Run the functions in 4 threads.
"""

from time import perf_counter
from threading import Thread
start_time = perf_counter()

def f1():
    for i in range(5):
        print(f"f1 - {i}")
 
def f2():
    for i in range(5):
        print(f"f2 - {i}")
 
def f3():
    for i in range(5):
        print(f"f3 - {i}")
       
def f4():
    for i in range(5):
        print(f"f4 - {i}")
