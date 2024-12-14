def transpose(matrix):
    res = []

    for i in range(len(matrix[0])):
        res.append([])

        for j in range(len(matrix)):
            res[i].append(matrix[j][i])

    return res

print (transpose([[5, 6, 7], [0, 3, 5]]))