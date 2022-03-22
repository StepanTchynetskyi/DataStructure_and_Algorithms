from number_loader import number_loader

def quick_sort(array):
    """faster than quick_sort_v1

    :param array:
    :return:
    """
    if len(array) <= 1:
        return array

    less_than_pivot = []
    greater_than_pivot = []
    pivot = array[0]
    for elem in array[1:]:
        if elem <= pivot:
            less_than_pivot.append(elem)
        else:
            greater_than_pivot.append(elem)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

numbers = number_loader("number.txt")
import time
start = time.time()
quick_sort(numbers)
end = time.time()
print(end-start)