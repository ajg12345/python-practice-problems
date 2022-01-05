"""
This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. 
That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
"""
from itertools import product


def num_of_x_in_n_grid(n: int, x: int) -> int:
    num_of_times = 0
    for i in range(n):
        for j in range(n):
            if (i + 1)*(j + 1) == x:
                num_of_times += 1

    return num_of_times


def num_of_x_in_n_grid_itertools(n: int, x: int) -> int:
    num_of_times = 0
    for i, j in product(range(n), range(n)):
        if (i + 1)*(j + 1) == x:
            num_of_times += 1
    return num_of_times


def Geeks_for_Geeks_answer(n: int, x: int):
    """It’s easy to see that number x can appear only once in a row. 
    If x contains in the ith row then the column number will be x/i. 
    x contains in the ith row if x is divisible by i. let’s check that 
    x divides i and x/i <= n. If these conditions met then update the answer."""
    ans = 0
    for i in range(1, n + 1):
        if (x % i == 0 and x / i <= n):
            ans += 1
    return ans


print(num_of_x_in_n_grid(6, 12))
print(num_of_x_in_n_grid_itertools(6, 12))
print(Geeks_for_Geeks_answer(6, 12))
