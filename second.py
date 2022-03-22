# 2
import random
array = [random.randint(0, 100) for n in range(0, 5)]

def main(array):
    highest_number = 0
    for n in array:
        if n > highest_number:
            highest_number = n
    return highest_number

if __name__ == '__main__':
    print(array)
    print(main(array))