def binary_search(array, target, precision=8):
    """Searches for value in sorted array, if value in array returns index of searched value, otherwise -1.
    Complexity = O(log(n))
    :param array: sorted array of numbers
    :param target: searched value
    :param precision: numbers after floating point to compare
    :return: index of searched value if it is found in array, otherwise -1
    """
    start = 0
    end = len(array) - 1
    target = round(target, precision)

    while start <= end:
        mid = (start + end) // 2
        if round(array[mid], precision) == target:
            return mid
        elif target > round(array[mid], precision):
            start = mid + 1
        else:
            end = mid - 1
    return -1

