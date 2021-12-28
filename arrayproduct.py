"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. 

If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from math import prod

def array_for_array(arr: list) -> list:
    return_array = []
    for i in range(len(arr)):
        return_array.append(prod(arr[0:i] + arr[i+1:]))
    return return_array


ex1 = [1, 2, 3, 4, 5]
ex2 = [3, 2, 1]
assert array_for_array(ex1) == [120, 60, 40, 30, 24]
assert array_for_array(ex2) == [2, 3, 6]

"""
The Geeks for Geeks answer is as follows below (its smart to note that the idea is to pass elements from the left to the right)
1. construct a temporary array left[] such that left[i] contains product of all elements on left of arr[i] excluding arr[i]
2. construct a temporary array right[] such that right[i] contains product of all elements on right of arr[i] excluding arr[i]
3. to get prod[], multiply left[] and right[]
"""

# and finally, the reason you can't use division is because you could simply get the total product and divide its total by each element 
#to get the resulting elements int the returned array