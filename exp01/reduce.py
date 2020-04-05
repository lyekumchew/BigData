import sys


def output(follower, followee):
    print("%s " % follower, end="")
    print(",".join(str(i) for i in followee))


def reducer():
    follower = None
    followee = []
    for line in sys.stdin:
        k, v = line.strip().split(':')  # 9:938
        if follower is None:
            follower = k
            followee.append(v)
        elif follower == k:
            followee.append(v)
        elif follower != k:
            output(follower, followee)
            followee = []
            follower = k
            followee.append(v)
    if len(followee) != 0:
        output(follower, followee)


if __name__ == '__main__':
    reducer()
