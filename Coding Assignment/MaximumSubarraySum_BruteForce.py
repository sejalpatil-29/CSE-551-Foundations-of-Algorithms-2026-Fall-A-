#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sejal Patil

from sys import maxsize                        # import max int for initialization

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]        # initialize the input array
ans = -maxsize - 1                             # initialize ans variable to -intmax

# WRITE YOUR CODE HERE
diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]  # daily price changes

for i in range(len(diff)):
    total = 0
    for j in range(i, len(diff)):
        total += diff[j]
        ans = max(ans, total)

print(ans)                                     # printing the answer