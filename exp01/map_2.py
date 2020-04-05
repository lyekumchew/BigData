import sys
from itertools import permutations


def mapper():
    for line in sys.stdin:
        key, values = line.strip().split(' ')
        if values.__contains__(','):
            perm_iterator = permutations(values.split(','), 2)
            for f in perm_iterator:
                print('%s_%s %s' % (f[0], f[1], key))


if __name__ == '__main__':
    mapper()
