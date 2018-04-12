#!/usr/bin/python3
def main():
    import sys
    sum = 0
    for i in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[i])
    print("{:i}".format(sum))

if __name__ == '__main__':
    main()
