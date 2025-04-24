#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    capitalized = [word.capitalize() for word in words]
    return ' '.join(capitalized)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
