import random
# array = [random.randint(1, 9) for n in range(0, 10)]
array = [6, 6, 6, 6, 6, 6, 2, 2, 2, 2]

def equal_secuence(array):
    max_sec = 0
    max_num = 0
    for n in range(1, 10):
        secuence = 0
        for i in range(0, len(array)):
            if array[i] != n:
                continue
            try:
                if array[i] == array[i + 1] or array[i] == array[i - 1]:
                    secuence += 1
            except:
                if array[i] == array[i - 1]:
                    secuence += 1
        if secuence > max_sec:
            max_sec = secuence
            max_num = n
    
    print(f'Longest: {max_sec}, Num: {max_num}')
        
print(array)
equal_secuence(array)



