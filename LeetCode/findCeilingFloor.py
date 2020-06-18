'''
Problem:

Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

Here is the definition of a node for the tree.
'''
class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.
  if root_node is None:
  	return (floor, ceil)

  if root_node.value == k:
  	return (k, k)

  if root_node.value > k:
 	ceil = root_node.value
	return findCeilingFloor(root_node.left, k, floor, ceil)

  else:
	floor = root_node.value
	return findCeilingFloor(root_node.right, k, floor, ceil)

root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print findCeilingFloor(root, 5)
# (4, 6)
