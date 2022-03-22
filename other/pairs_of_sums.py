
# Write function to find all pairs of an integer array whose sum is equal to a given number
# Input [2,4,3,5,6,-2,4,7,8,9]
# Output: ['2+5', '4+3', '3+4', '-2+9']

def pair_sum(arr, sum_):
    res = []
    temp = {}
    for i in range(len(arr)):
        difference = sum_ - arr[i]
        if temp.get(difference, None) is not None:
            res.append(str(arr[i]) + "+" + str(difference))
        temp[arr[i]] = i
    return res

print(pair_sum([2,4,3,5,6,-2,4,7,8,9],7))