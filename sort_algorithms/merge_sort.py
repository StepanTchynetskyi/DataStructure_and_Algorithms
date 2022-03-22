def split(array):
    mid = len(array)//2
    return array[:mid], array[mid:]


def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def merge_sort(array):
    """
    O(kn log n)
    k - length of slicing
    log n - splitting
    n - sorting in merge function
    :param array:
    :return:
    """
    if len(array) <= 1:
        return array

    left_half, right_half = split(array)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
