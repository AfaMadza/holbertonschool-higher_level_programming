#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    flag = 1
    pos_num = -1 * number
elif number > 0:
    flag = 0
    pos_num = number
n = pos_num % 10
if flag == 1:
    n = -1 * n
if n > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, n))
elif n == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, n))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, n))
