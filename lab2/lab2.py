def split(s):
    return [char for char in s]


if __name__ == '__main__':
    f = open('file.txt')
    numbers = f.read().split('\n')

    for el, i in zip(numbers, range(0, numbers.__len__())):
        numbers[i] = split(el)

    for r in numbers:
        for x in r:
            print("%3s" % x, end=' ')
        print()
