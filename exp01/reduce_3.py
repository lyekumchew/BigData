import sys
import heapq


def print_top_10(k, top_10):
    print(k, end=":")
    print(" ".join(str(x[0]) for x in top_10))


def reducer():
    key = None
    temp_list = []

    for line in sys.stdin:
        k, v = line.strip().split(' ')  # 726_856 2
        p1, p2 = k.split('_')  # 726_856
        if key is None:
            key = p1
            temp_list.append((p2, v))
        elif p1 == key:
            temp_list.append((p2, v))
        elif p1 != key:
            top_10 = heapq.nlargest(10, temp_list, key=lambda x: int(x[1]))
            print_top_10(key, top_10)
            key = p1
            temp_list = []
            temp_list.append((p2, v))

    if len(temp_list) != 0:
        top_10 = heapq.nlargest(10, temp_list, key=lambda x: int(x[1]))
        print_top_10(key, top_10)


if __name__ == '__main__':
    reducer()
