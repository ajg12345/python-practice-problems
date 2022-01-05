"""
This problem was asked by Microsoft. (Easy)

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.
  1
 / \
2   3
   / \
  4   5
"""

# a good answer here would be to enqueue the node values and then print that queue
# https://www.geeksforgeeks.org/print-level-order-traversal-line-line/
# but before i can do this, I'll have to figure out a python representation
# https://www.youtube.com/watch?v=5kaVCwKd3hI
# so lets look at implementing a binary search tree:
from dataclasses import dataclass
from typing import Any


@dataclass
class BST():
    value: Any
    left: 'BST' = None
    right: 'BST' = None

# and here's an answer to resolve the question:


def printLevelOrder(root):
    if root is None:
        return
    # Create an empty queue for level order traversal
    q = []
    q.append(root)
    while q:
        count = len(q)
        while count > 0:
            temp = q.pop(0)
            print(temp.value, end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

            count -= 1
        print(' ')


# Driver Code
root = BST(1)
root.left = BST(2)
root.right = BST(3)
root.right.left = BST(4)
root.right.right = BST(5)

printLevelOrder(root)

# This code is contributed by Praveen kumar
