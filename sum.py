import random

array = [random.randint(0, 9) for n in range(0, 9)]


def target_sum(target, array):
    for i in range(len(array) - 1):
        first_num = array[i]
        for n in range(i + 1, len(array)):
            second_num = array[n]
            if first_num + second_num == target:
                return [first_num, second_num]
    return []

if __name__ == '__main__':
    target = 10
    print(array)
    print(target_sum(target, array))
 