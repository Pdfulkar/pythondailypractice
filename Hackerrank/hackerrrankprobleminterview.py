#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    count = 0
    lev = 0
    # for i in path:
    #     if i == "U":
    #         sea_level +=1
    #         lev+=1
    #     if i == "D":
    #         sea_level-=1
    #         lev+=1
    #     if sea_level== 0 and path[lev+1 if lev +1 in range(len(path)) else 0]== "D":
    #         count+=1
    # return count
    counter = 0
    result = 0
    for i in path:
        if i =="U":
            counter += 1
            if counter == 0:
                result += 1
        if i=="D":
            counter -=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()