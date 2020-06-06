'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Copyright © 2020 LeetCode

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #solve recursively
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, minValue, maxValue):
        if not root:
            return True

        if (root.val <= minValue) or (root.val >= maxValue):
            return False

        validLeft = self.helper(root.left, minValue, root.val)
        validRight = self.helper(root.right, root.val, maxValue)

        return validLeft and validRight
