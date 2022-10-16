# Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero)

def underDiagonalZero(mat, n, m):
 
    for i in range(n):
        for j in range(m):
            if (i > j):
                mat[i][j] = 0

    for i in range(n):
        for j in range(m):
            print( mat[i][j], end = " ")
        print()

n = 4
m = 4
mat = [[ 2, 1, 7, 24 ],
       [ 3, 7, 2, 30 ],
       [ 5, 4, 9, 19 ],
       [ 11, 12, 13, 14 ]]
 
underDiagonalZero(mat, n, m)