# Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order

def convert_to_matrix(string, K):

   # slicing strings
   temp = [string[index: index + K] for index in range(0, len(string), K)]
   # conversion to list of characters
   res = [list(element) for element in temp]
   return res


def printSpiralOrder(mat):

    if len(mat) == 0:
        return
 
    top = left = 0
    bottom = len(mat) - 1
    right = len(mat[0]) - 1
 
    while True:
        if left > right:
            break
 
        # print top row:  i=[0, len(mat[0]) - 1]  00 01 02...0(K-1)
        for i in range(left, right + 1):
            print(mat[top][i], end='')
        top = top + 1
 
        if top > bottom:
            break
 
        # print right column:  i=[1, len(mat) - 1]  1(K-1) 2(K-1)...(K-1)(K-1)
        for i in range(top, bottom + 1):
            print(mat[i][right], end='')
        right = right - 1
 
        if left > right:
            break
 
        # print bottom row:  i=[len(mat[0]) - 2, 0]  (K-1)(K-2) (K-1)(K-3)...(K-1)0
        for i in range(right, left - 1, -1):
            print(mat[bottom][i], end='')
        bottom = bottom - 1
 
        if top > bottom:
            break
 
        # print left column:  i=[len(mat) - 2, 1]   (K-2)0 (K-1)0... 10
        for i in range(bottom, top - 1, -1):
            print(mat[i][left], end='')
        left = left + 1
 

string = 'firsn_ltoba_htyp'

print("K x K matrix, K= :")
K = int(input())

mat= convert_to_matrix(string, K)
printSpiralOrder(mat)