import sys


def mapper():
    for line in sys.stdin:
        follower, followee = line.strip().split(':')
        followee = followee.strip().split(' ')
        for f in followee:
            print("%s:%s" % (f, follower))


if __name__ == '__main__':
    mapper()
