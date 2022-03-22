def recursive_binary_search(array, target, precision=8):
    target = round(target, precision)
    if len(array) == 0:
        return False
    else:
        mid = len(array) // 2
        if round(array[mid], precision) == target:
            return True
        elif target > round(array[mid], precision):
            return recursive_binary_search(array[mid+1:], target)
        else:
            return recursive_binary_search(array[:mid], target)