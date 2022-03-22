def board(n):
    if n > 10:
        n = 5
        print('El número es mayor a 10, lo bajamos a 5!')
    x = 1
    table = ''
    while x <= n**2:
        if x % 2 != 0:
            table += 'X'
        else:
            table += '_'
        if x % n == 0:
            table += '\n'
        x += 1
    return table

print(board(12))