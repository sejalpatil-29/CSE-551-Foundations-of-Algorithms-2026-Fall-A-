#!/usr/bin/env python3
import random
# -*- coding: utf-8 -*-
#@author: Sejal Patil

input_text = "algorithms"

# Generate random enumeration of letters (Random Sequential Order)
n = len(input_text)
randomOrder = [None] * n
for i in range(n):
    randomOrder[i] = i

for i in range(n-1):
    randPos = i + random.randint(0, n-i-1)
    tmp = randomOrder[i];
    randomOrder[i] = randomOrder[randPos];
    randomOrder[randPos] = tmp;

letters = list(input_text)
moved = [False] * n

for i in range(n):
    pick = randomOrder[i]
    if moved[pick]:
        continue

    direction = random.choice([-1, 1])
    target = pick + direction

    if target < 0 or target >= n:
        continue
    if moved[target]:
        continue

    letters[pick], letters[target] = letters[target], letters[pick]
    moved[pick] = True
    moved[target] = True

print("Result: " + "".join(letters))