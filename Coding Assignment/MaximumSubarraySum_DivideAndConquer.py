#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sejal Patil

from sys import maxsize                              # import max int for initialization

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]        # initialize the input array
ans = -maxsize - 1                             # initialize ans variable to -intmax

# WRITE YOUR CODE HERE
def max_crossing_sum(diff, low, mid, high):
    left_sum = -maxsize - 1
    total = 0
    for i in range(mid, low - 1, -1):
        total += diff[i]
        left_sum = max(left_sum, total)

    right_sum = -maxsize - 1
    total = 0
    for i in range(mid + 1, high + 1):
        total += diff[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum

def max_subarray_sum(diff, low, high):
    if low == high:
        return diff[low]

    mid = (low + high) // 2
    return max(max_subarray_sum(diff, low, mid),
               max_subarray_sum(diff, mid + 1, high),
               max_crossing_sum(diff, low, mid, high))

diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]  # daily price changes
ans = max_subarray_sum(diff, 0, len(diff) - 1)

print(ans)                                     # printing the answer