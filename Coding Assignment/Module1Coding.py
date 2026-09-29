#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: SEJAL PATIL


''' --- Input values --- '''
M = [ [2, 1, 4, 5, 3],              # Department preference list
     [4, 2, 1, 3, 5], 
     [2, 5, 3, 4, 1], 
     [1, 4, 3, 2, 5], 
     [2, 4, 1, 5, 3] ]
W = [ [5, 1, 2, 4, 3],              # Employee preference list
     [3, 2, 4, 1, 5], 
     [2, 3, 4, 5, 1], 
     [1, 5, 4, 3, 2], 
     [4, 2, 5, 3, 1] ]
N = 5                               # Number of department & employee



# WRITE YOUR CODE HERE

# Create ranking table for employee preferences
rank = [[0] * N for _ in range(N)]

for employee_id in range(N):
    for position in range(N):
        department_id = W[employee_id][position]
        rank[employee_id][department_id - 1] = position

employee = [0] * N
next_choice = [0] * N
free_departments = list(range(N))

while free_departments:
    department = free_departments.pop(0)
    employee_id = M[department][next_choice[department]]
    next_choice[department] += 1
    employee_index = employee_id - 1

    if employee[employee_index] == 0:
        employee[employee_index] = department + 1

    else:
        current_department = employee[employee_index] - 1
        if rank[employee_index][department] < rank[employee_index][current_department]:
            employee[employee_index] = department + 1
            free_departments.append(current_department)
        else:
            free_departments.append(department)


''' --- Visualizing the result, Printing the output --- '''
Names = [ ['HR', 'CRM', 'Admin', 'Research', 'Development'],      # Initialize the mapping of names
         ['Adam', 'Bob', 'Clare', 'Diane', 'Emily'] ]
print('Result is:-')
for i in range(N):
    print(Names[0][i], ":", Names[1][employee[i]-1])                # Map the result to the names


