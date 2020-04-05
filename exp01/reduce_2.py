import sys


def output(k, v):
    print("%s %s" % (k, v))


def reducer():
    key = None
    tmp = 0
    for line in sys.stdin:
        k, v = line.split(' ')
        if key is None:
            key = k
            tmp += 1
        elif key == k:
            tmp += 1
        elif key != k:
            output(key, tmp)
            key = k
            tmp = 0
            tmp += 1
    if tmp != 0:
        output(key, tmp)


if __name__ == '__main__':
    reducer()
