"""
This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""


def smallest_int_not_sum_of_subset(arr: list) -> int:
    result = 1
    for e in arr:
        if result < e:
            return result
        result += e
    return result


# test cases

b = [1, 2, 3, 10]

assert smallest_int_not_sum_of_subset(b) == 7

a = [1, 2, 3, 7, 45]
a.sort()

assert (smallest_int_not_sum_of_subset(a)) == 14

arr1 = [1, 3, 4, 5]
assert (smallest_int_not_sum_of_subset(arr1)) == 2

arr2 = [1, 2, 6, 10, 11, 15]
assert (smallest_int_not_sum_of_subset(arr2)) == 4

arr3 = [1, 1, 1, 1]
assert (smallest_int_not_sum_of_subset(arr3)) == 5

arr4 = [1, 1, 3, 4]
assert (smallest_int_not_sum_of_subset(arr4)) == 10
