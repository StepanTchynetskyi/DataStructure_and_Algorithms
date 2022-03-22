def insertion_sort(array):
    """
    best: O(n)
    worst: O(n^2)
    :param array:
    :return:
    """

    for i in range(1, len(array)):
        key = array[i]

        j = i -1
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key

from number_loader import number_loader
numbers = number_loader("number.txt")
insertion_sort(numbers)
print(numbers)