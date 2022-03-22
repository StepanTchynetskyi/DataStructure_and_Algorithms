import random


def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True


def bogo_sort(array):
    while not is_sorted(array):
        random.shuffle(array)
    return array

numbers = [1, 5, 1, 3, 5, 1, 4, 6, 43, 4, 5]
bogo_sort(numbers)
print(numbers)
