#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sejal Patil

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]        # initialize the input array

# WRITE YOUR CODE HERE
diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]  # daily price changes

ans = diff[0]
cur = diff[0]
for i in range(1, len(diff)):
    cur = max(diff[i], cur + diff[i])
    ans = max(ans, cur)

print(ans)                                     # printing the max possible subarray sum, as ans