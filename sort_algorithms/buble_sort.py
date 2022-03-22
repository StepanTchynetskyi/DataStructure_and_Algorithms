def bubble_sort_bad(array):
    """Bad implementation of bubble sort
    O(n^2)
    :param array:
    :return:
    """
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def bubble_sort(array):
    """Implementation of bubble sort
        O(n^2)
        :param array:
        :return:
        """
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
