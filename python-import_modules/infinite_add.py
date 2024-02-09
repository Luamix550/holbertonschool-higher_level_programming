#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lentgh = len(sys.argv)
    j = 0
    for i in range(1, lentgh):
        j += (int(sys.argv[i]))
    print("{}".format(j))
