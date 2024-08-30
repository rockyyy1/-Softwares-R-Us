# Sorting a list in the simplest way possible\

from typing import Iterable
import random

sort_me = [random.randint(0, 100) for i in range(10)]


def rocky_sort(sort_me: Iterable) -> list:
    """Returns a sorted list of integers"""
    sorted_list = []
    for number in sort_me:
        if number < number + 1:
            sorted_list.append(number)
    return sorted_list

print("Unsorted: ", sort_me)
print("Sorted:  ", rocky_sort(sort_me))
