#!/usr/bin/python3
import sys


def main(argv):
    sum = 0
    for i in range(1, len(argv)):
        sum = sum + int(argv[i])
    print("{:d}".format(sum))

if __name__ == '__main__':
    main(sys.argv)
