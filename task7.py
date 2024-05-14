import random
import math

def my_func():
    arr = []
    for i in range(5):
        num = random.randint(20, 50)
        if num % 2 == 0:
            num = int(math.pow(num, 2))
        arr.append(num)
    return arr

print(my_func())