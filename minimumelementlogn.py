"""
This problem was asked by Uber.

Suppose an array sorted in ascending order is 
rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""
from math import floor


def findlowest(arr: list) -> int:
    length = len(arr)
    if length == 2:
        return arr[0] if arr[1] > arr[0] else arr[1]
    if length == 1:
        return arr[0]
    beginning = arr[0]
    middle = arr[floor(length/2)]
    last = arr[-1]
    #6, 2, 5
    if beginning > middle:
        return findlowest(arr[0:floor(length/2)+1])
    #5, 6, 2
    if middle > last:
        return findlowest(arr[floor(length/2):])
    # 2, 5 6
    if last > beginning:
        return beginning


assert findlowest([5, 7, 10, 3, 4]) == 3
assert findlowest([3, 4, 5, 7, 10]) == 3
assert findlowest([10, 11, 4]) == 4
