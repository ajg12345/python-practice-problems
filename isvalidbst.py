'''
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the 
key in the left child must be less than or equal to the root and the key in the right 
child must be greater than or equal to the root.
'''
#first we implement the BST class:
from dataclasses import dataclass
from typing import Any

@dataclass
class BST():
    value: Any
    left: 'BST' = None
    right: 'BST' = None

def isvalidnode(BST: BST):
    if not BST.left and not BST.right:
        return True
    elif BST.left and BST.right:
        return BST.value > BST.left.value and BST.value < BST.right.value
    elif BST.left and not BST.right:
        return BST.value > BST.left.value 
    else:
        return BST.value < BST.right.value

def isvalidBST(BST: BST):
    if isvalidnode(BST):
        if BST.left and BST.right:
            return isvalidBST(BST.left) and isvalidBST(BST.right)
        elif BST.left and not BST.right:
            return isvalidBST(BST.left) 
        elif not BST.left and BST.right:
            return isvalidBST(BST.right) 
        else:
            return True
    else: 
        return False

a = BST(10)
a.left = BST(2)
a.right = BST(20)

b = BST(10)
b.left = BST(12)
b.right = BST(20)

c = BST(10)
c.left = BST(2)
c.right = BST(20)
c.right.left = BST(25)


assert isvalidBST(a) == True
assert isvalidBST(b) == False
assert isvalidBST(c) == False
