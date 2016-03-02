import io


def read_file():
    f = io.open('sherlock_small.txt', 'r')
    print(f.name)

    # for line in f:
    #     print(line)

read_file()

