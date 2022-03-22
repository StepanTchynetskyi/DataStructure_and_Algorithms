def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quick_sort(array, *, low=0, high=None):
    """
    If array lenght is less than 17 use insertion sort algorithm
    O(n^2) - worst
    O(n * log n)
    :param array:
    :param low:
    :param high:
    :return:
    """
    if high is None:
        high = len(array) - 1

    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low=low, high=pi-1)
        quick_sort(array, low=pi+1, high=high)
