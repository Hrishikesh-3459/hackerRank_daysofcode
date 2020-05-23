#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    x = bin(n).replace("0b", "")
    i = 0
    max_count = 0
    temp = 0
    while (i < len(x)):
        cur = x[i]
        if (cur == '1'):
            temp += 1
        else:
            if (temp > max_count):
                max_count = temp
            temp = 0
        i += 1
    print(max(max_count, temp))
