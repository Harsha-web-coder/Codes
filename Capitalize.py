#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l=s.split(" ")
    n=len(l)
    S=""
    for i in range(n):
        S=S+l[i].capitalize()+" "
        """
        s=l[i][0].upper()        
        x=str(s+l[i][1:])
        S=S+x+" "
        return S
        """
    return S
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
"""

Sample Input

chris alan
Sample Output

Chris Alan
"""
#we can use print(s.title())