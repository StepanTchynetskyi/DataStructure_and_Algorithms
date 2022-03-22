def merge(array, left, mid, right):
    index_after_mid = mid + 1
    i = left
    j = index_after_mid
    res = []
    while i < index_after_mid and j <= right:
        if array[i] < array[j]:
            res.append(array[i])
            i += 1
        else:
            res.append(array[j])
            j += 1
    while i < index_after_mid:
        res.append(array[i])
        i += 1
    while j < right:
        res.append(array[j])
        j += 1
    for i in res:
        array[left] = i
        left += 1


def iterative_merge_sort(array):
    low = 0
    high = len(array) - 1
    width = 1
    while width <= high - low:
        for i in range(low, high, 2 * width):
            left = i
            mid = i + width - 1
            right = min(i + 2 * width - 1, high)
            merge(array, left, mid, right)
        width = 2 * width
