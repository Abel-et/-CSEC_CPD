 matrix =[]
    for i in range(5):
        mat = list(map(int,input().split()))
        matrix.append(mat)
    position = [[i, j] for i in range(5) for j in range(5) if matrix[i][j] == 1]
    print(position)
    row = position[0][0]
    coloumn = position[0][1]
    min_swap = abs(row-2)+ abs(coloumn-2)
    return min_swap
