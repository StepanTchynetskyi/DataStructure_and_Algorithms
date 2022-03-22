def rotate_matrix(array):
    n = len(array)

    for i in range(n//2):
        for j in range(i, n-i-1):
            top = array[i][j]
            array[i][j] = array[n-j-1][i]
            array[n-j-1][i] = array[n-i-1][n-j-1]
            array[n - i - 1][n - j - 1] = array[j][n-i-1]
            array[j][n - i - 1] = top

A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
rotate_matrix(A)
for i in A:
    print(i)