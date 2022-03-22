array = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a']

def is_symetric(array):
    if array[::] == array[::-1]:
        return "Symetric!"
    return "Asymetric :("


if __name__ == '__main__':
    print(is_symetric(array))