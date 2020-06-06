'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Copyright © 2020 LeetCode

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #If empty root, it will return True
        if not root:
            return True
        #Oterwise call recursive helper function to check left and right subtree
        return self.helper(root.left, root.right)

    def helper(self, leftSub, rightSub):
        #Check if leftSub and rightSub exist.If not exist return True
        if (leftSub == None) and (rightSub == None):
            return True
        #If any of left or right sub tree exist, check recursively again
        elif (leftSub != None) and (rightSub != None):
            return (leftSub.val == rightSub.val) and self.helper(leftSub.left,rightSub.right) and self.helper(leftSub.right,rightSub.left)
        else:
            return False
