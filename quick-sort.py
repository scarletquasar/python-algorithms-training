from numbers import Number
import random

def quicksort(list):
    if len(list) < 2:
        return list

    left = [] 
    middle = [] 
    right = []
    
    pivot = random.choice(list)

    for item in list:
        if item < pivot:
            left.append(item)
        if item == pivot:
            middle.append(item)
        if item > pivot:
            right.append(item)

    return quicksort(left) + middle + quicksort(right)


print(quicksort([300, 242, -1, 23, 1, 2, 4, 32, 1]))
