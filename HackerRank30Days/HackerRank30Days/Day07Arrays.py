#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
rarr = ""
i = n-1
while i >= 0:
    rarr = rarr + str(arr[i]) + " "
    i -= 1
print rarr

