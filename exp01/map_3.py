import sys


def mapper():
    for line in sys.stdin:
        k, v = line.strip().split(" ")  # 0_118 2
        p1, p2 = k.split("_")  # 0_118
        print("%s_%s %s" % (p1, p2, v))
        # print("%s_%s %s" % (p2, p1, v))


if __name__ == '__main__':
    mapper()
