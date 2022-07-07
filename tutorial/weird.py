#!/bin/python3

import math
import os
import random
import re
import sys

"""
- If n is odd, print Weird
- If n is even and in the inclusive range of 2 to 5, print Not Weird
- If n is even and in the inclusive range of 6 to 20, print Weird
- If n is even and greater than 20, print Not Weird
"""
if __name__ == '__main__':
    n = int(input().strip())
    # Order from most common check to least
    if n % 2 == 1:
        print("Weird")
    elif n > 20 or n < 5:
        print("Not Weird")
    else:
        print("Weird")
