def partition(array, low, high):
    if array[low] > array[high]:
        array[low], array[high] = array[high], array[low]
    j = k = low + 1
    left_pivot, right_pivot = array[low], array[high]
    stop = high - 1
    while k <= stop:
        if array[k] < left_pivot:
            array[k], array[j] = array[j], array[k]
            j += 1
        elif array[k] >= right_pivot:
            while array[stop] > right_pivot and k < stop:
                stop -= 1
            array[k], array[stop] = array[stop], array[k]
            stop -= 1
            if array[k] < left_pivot:
                array[k], array[j] = array[j], array[k]
                j += 1

        k += 1
    j -= 1
    stop += 1
    array[low], array[j] = array[j], array[low]
    array[high], array[stop] = array[stop], array[high]
    return j, stop


def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        left_pivot, right_pivot = partition(array, low, high)
        quick_sort(array, low, left_pivot - 1)
        quick_sort(array, left_pivot + 1, right_pivot - 1)
        quick_sort(array, right_pivot + 1, high)



