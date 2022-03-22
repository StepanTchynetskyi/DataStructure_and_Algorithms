def merge(array, start, end, mid):
    index_after_mid = mid + 1
    left_index = start
    right_index = index_after_mid
    res = []
    while left_index < index_after_mid and right_index <= end:
        if array[left_index] < array[right_index]:
            res.append(array[left_index])
            left_index += 1
        else:
            res.append(array[right_index])
            right_index += 1
    while left_index < index_after_mid:
        res.append(array[left_index])
        left_index += 1
    while right_index < end:
        res.append(array[right_index])
        right_index += 1
    for i in res:
        array[start] = i
        start += 1


def merge_sort(array, *, left=0, right=None):
    """Inplace merge sort algorithm
    :param array:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        mid = left + (right - left) // 2
        # if left < mid:
        merge_sort(array, left=left, right=mid)
        # if mid + 1 < right and right - left != 1:
        merge_sort(array, left=mid + 1, right=right)
        return merge(array, start=left, end=right, mid=mid)

numbers = [1,2,5,4,5,63,14,62,73,41,1,35,51]
merge_sort(numbers, left=0, right=len(numbers) - 1)
print(numbers)