"""
This problem was asked by Facebook.

Suppose you are given two lists of n points, one list p1, p2, ..., pn 
on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. 
Imagine a set of n line segments connecting each point pi to qi. 

Write an algorithm to determine how many pairs of the line segments intersect.
"""


def check_intersection(p: list, q: list) -> int:
    intersecting_pair_count = 0
    if len(p) <= 1:
        return intersecting_pair_count
    for i in range(len(p)):
        pi = p[i]
        qi = q[i]
        for j in range(len(p)):
            if j == i:
                continue
            pj = p[j]
            qj = q[j]
            # lines have an intersecting endpoint
            if pj == pi or qj == qi:
                intersecting_pair_count += 1
            # i line foward slant and j line backward slant
            elif qi > qj and pi < pj:
                intersecting_pair_count += 1
            # i line backward slant and j line forward slant
            elif qi < qj and pi > pj:
                intersecting_pair_count += 1
    return int(intersecting_pair_count / 2)


# test lists:
q = [0, 6, 3, 0]
p = [1, 5, 0, 2]
assert check_intersection(p, q) == 3

q = [2, 1]
p = [0, 1]
assert check_intersection(p, q) == 1
