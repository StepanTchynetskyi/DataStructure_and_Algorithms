from typing import List, Union


def linear_search(array: List[Union[int, float]], target: Union[int, float], precision=8):
    """Searches for value in array, if value in array returns index of searched value, otherwise -1.
    Complexity = O(n)
    :param array: unordered list of Numbers, where target value
    :type array: List[int, float]
    :param target: searched value
    :type target: Union[int, float]
    :param precision: numbers after floating point to compare
    :type precision: int
    :return: index of searched value if it is found in array, otherwise -1
    """
    for i in range(len(array)):
        if round(array[i], precision) == round(target, precision):

            return i
    return -1

