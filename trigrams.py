import io


def read_file():
    f = io.open('sherlock_small.txt', 'r')
    lines = f.readlines()
    print(lines)
    return lines

read_file()

