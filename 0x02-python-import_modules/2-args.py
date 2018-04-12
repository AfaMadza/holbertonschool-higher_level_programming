#!/usr/bin/python3
def main():
    import sys
    flag = 0
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {:s}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        for i in range(1, len(sys.argv)):
            if flag == 0:
                print("{:d} arguments:".format(len(sys.argv) - 1))
            flag = 1
            print("{:d}: {:s}".format(i, sys.argv[i]))
if __name__ == '__main__':
    main()
