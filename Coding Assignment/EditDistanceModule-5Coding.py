#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sejal Patil

w1 = "professor"
w2 = "confession"
ans = 0                                   

memo = {}

def edit_distance(i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    if (i, j) in memo:
        return memo[(i, j)]
    if w1[i - 1] == w2[j - 1]:
        result = edit_distance(i - 1, j - 1)
    else:
        insert = edit_distance(i, j - 1)
        delete = edit_distance(i - 1, j)
        replace = edit_distance(i - 1, j - 1)
        result = 1 + min(insert, delete, replace)
    memo[(i, j)] = result
    return result

def backtrack(i, j):
    operations = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and w1[i - 1] == w2[j - 1]:
            i, j = i - 1, j - 1
        elif i > 0 and j > 0 and edit_distance(i, j) == edit_distance(i - 1, j - 1) + 1:
            operations.append(f"Replace '{w1[i - 1]}' with '{w2[j - 1]}' at position {i - 1}")
            i, j = i - 1, j - 1
        elif j > 0 and edit_distance(i, j) == edit_distance(i, j - 1) + 1:
            operations.append(f"Insert '{w2[j - 1]}' at position {i}")
            j -= 1
        else:
            operations.append(f"Delete '{w1[i - 1]}' at position {i - 1}")
            i -= 1
    operations.reverse()
    return operations

ans = edit_distance(len(w1), len(w2))

for op in backtrack(len(w1), len(w2)):
    print(op)

print(ans)                                     