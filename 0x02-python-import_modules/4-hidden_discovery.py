#!/usr/bin/python3
def main():
    import hidden_4
    names = dir(hidden_4)
    for i in range(0, len(names)):
        if names[i][0] != '_':
            print("{:s}".format(names[i]))
if __name__ == '__main__':
    main()
