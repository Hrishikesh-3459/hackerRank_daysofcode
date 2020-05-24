#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = -100
    row = 0
    col = 0
    cur = 0
    while (row + 2 != 6):
        for i in range(3):
            for j in range(3):
                if (i == 1):
                    cur += arr[row + i][col + 1]
                    break
                cur += arr[row + i][col + j]
        if(cur > max_sum):
            max_sum = cur
        cur = 0
        col += 1
        if(col == 4):
            row += 1
            col = 0
        
    print(max_sum)
    
