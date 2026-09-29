#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sejal

# Union-Find (Disjoint Set) data structure, implemented from scratch
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]] 
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


# Function to perform Kruskal's algorithm for single link k-clustering
def greedy_clustering_kruskal(distance_matrix, k):
    n = len(distance_matrix)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((distance_matrix[i][j], i, j))
    edges.sort(key=lambda e: e[0])

    uf = UnionFind(n)
    num_clusters = n

    for weight, i, j in edges:
        if num_clusters == k:
            break
        if uf.union(i, j):
            num_clusters -= 1

    # Group vertices by their root representative
    clusters = {}
    for v in range(n):
        root = uf.find(v)
        clusters.setdefault(root, []).append(v)

    return list(clusters.values())  


# Use this input
distance_matrix = [
    [0, 38, 17, 28, 88, 59, 13],
    [38, 0, 52, 49, 83, 91, 59],
    [17, 52, 0, 46, 34, 77, 80],
    [28, 49, 46, 0, 5, 53, 62],
    [88, 83, 34, 5, 0, 43, 33],
    [59, 91, 77, 53, 43, 0, 27],
    [13, 59, 80, 62, 33, 27, 0]
]

# Set k=2 for number of clusters
k = 2
clusters = greedy_clustering_kruskal(distance_matrix, k)

print("Resulting Clusters:", clusters)
