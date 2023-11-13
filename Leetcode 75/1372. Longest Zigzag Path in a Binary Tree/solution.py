# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigZag(self, root: Optional[TreeNode], direction: str, length: int) -> None:
        if not root:
            return

        if (length > self.max_length):
            self.max_length = length

        if direction != "right":
            self.zigZag(root.right, "right", length + 1)
        else:
            self.zigZag(root.right, "right", 1)

        if direction != "left":
            self.zigZag(root.left, "left", length + 1)
        else:
            self.zigZag(root.left, "left", 1) 

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        self.zigZag(root, "", 0)
        return self.max_length
 