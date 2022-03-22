def recursive_binary_search(array, target, precision=8, *, start=0, end=None):
    """Searches for value in sorted array, if value in array returns index of searched value, otherwise -1.
    Complexity = O(log(n))
    :param array: sorted array of numbers
    :param target: searched value
    :param precision: numbers after floating point to compare
    :param start: the start position to search in array
    :param end: the end position to search in array
    :return: index of searched value if it is found in array, otherwise -1
    """
    if end is None:
        end = len(array) - 1
    if start > end:
        return -1
    target = round(target, precision)
    mid = (start + end) // 2
    if round(array[mid], precision) == target:
        return mid
    elif target > round(array[mid], precision):
        return recursive_binary_search(array, target, start=mid+1, end=end)
    else:
        return recursive_binary_search(array, target, start=start, end=mid-1)


