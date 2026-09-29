#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sejal Patil

# Define the graph structure based on skill matches
engineers = ['s1', 's2', 's3', 's4', 's5']
projects = ['p1', 'p2', 'p3', 'p4', 'p5']

# Adjacency list: which engineers can work on which projects
adjacency_list = {
    's1': ['p1', 'p2'],
    's2': ['p2'],
    's3': ['p1', 'p3', 'p4'],
    's4': ['p2', 'p4'],
    's5': ['p2', 'p5']
}

# Special constraints
max_assignments = {
    's1': 1, 's2': 1, 's3': 2, 's4': 1, 's5': 1,  # Engineers
    'p1': 1, 'p2': 2, 'p3': 1, 'p4': 1, 'p5': 1    # Projects
}

# Keep track of assignments
engineer_to_project = {}  # Map of engineer -> list of projects
project_to_engineers = {}  # Map of project -> list of engineers

# Initialize empty assignments
for e in engineers:
    engineer_to_project[e] = []
for p in projects:
    project_to_engineers[p] = []

def dfs(engineer, visited):
    """Depth-first search to find augmenting path"""
    # Try each project the engineer can work on
    for project in adjacency_list[engineer]:
        if project not in visited:
            visited.add(project)
            
            # If project can accept more engineers or we can reassign
            if (len(project_to_engineers[project]) < max_assignments[project] or
                any(dfs(e, visited) for e in project_to_engineers[project])):
                
                # If the engineer can take another assignment
                if len(engineer_to_project[engineer]) < max_assignments[engineer]:
                    # Assign project to engineer
                    engineer_to_project[engineer].append(project)
                    project_to_engineers[project].append(engineer)
                    return True
    
    return False

def maximum_bipartite_matching():
    for engineer in engineers:
        while len(engineer_to_project[engineer]) < max_assignments[engineer]:
            visited = set()
            if not dfs(engineer, visited):
                break
    return sum(len(assigned) for assigned in engineer_to_project.values())

# Run the maximum bipartite matching algorithm
total_assignments = maximum_bipartite_matching()

print("Maximum number of assignments: " + str(total_assignments))
print("\nAssignments:")
for engineer in engineers:
    for project in engineer_to_project[engineer]:
        print(engineer + " -> " + project)