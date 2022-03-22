def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    start = [0]
    end = [0]
    for i in range(len(s)):
        temp_arr = [s[i]]
        for j in range(i + 1, len(s) + 1):
            if j == len(s) or s[j] in temp_arr:
                if len(temp_arr) > end[-1] - start[-1]:
                    start = [i]
                    end = [j]
                elif len(temp_arr) == end[-1] - start[-1]:
                    print(end[-1] - start[-1])
                    start.append(i)
                    end.append(j)

                break
            temp_arr.append(s[j])
        print(temp_arr)
    start_idx = start[0]
    end_idx = end[0]
    for i in range(1, len(start)):
        temp_start = start[i]
        temp_end = end[i]
        temp_start1 = start_idx
        while temp_start < temp_end:
            if s[temp_start] < s[temp_start1]:
                start_idx = start[i]
                end_idx = end[i]
                break
            elif s[temp_start] > s[start_idx]:
                break
            else:
                temp_start += 1
                temp_start1 += 1
    return s[start_idx:end_idx]


print(removeDuplicateLetters("bcabc"))