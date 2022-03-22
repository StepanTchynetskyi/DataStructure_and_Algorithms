def inplace_selection_sort(array):
    """
    O(n^2)
    :param array:
    :return:
    """
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def selection_sort(array):
    sorted_array = []
    for i in range(len(array)):
        min_index = 0
        for j in range(1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        sorted_array.append(array.pop(min_index))
    return sorted_array
