import random
array = [random.randint(1, 5) for n in range(0, 10)]

def histogram(array):
    for n in range(1, 6):
        ocurrencies = array.count(n)
        pin = '*' * ocurrencies
        print(f'{n}: {pin}')

if __name__ == '__main__':
    print(array)
    histogram(array)