import random

# n = random.randint(0, 9)
n = 5

print('Matriz: ', n, 'x', n)

if n == 0:
    print('Error')
    exit()

matrix = [['' for x in range(n)] for x in range(n)]

def matrix_challenge(matrix):
    i = 0
    i_back = 1
    while i < len(matrix):
        matrix[i][i] = 'X'
        matrix[i][-i_back] = 'X'
        i += 1
        i_back += 1
    for item in matrix:
        print(item)


matrix_challenge(matrix)

