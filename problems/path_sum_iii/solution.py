# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def startPath(self, root: Optional[TreeNode], remainingSum: int) -> int:
        if not root:
            return 0

        if root.val == remainingSum:
            return 1 + self.startPath(root.left, 0) + self.startPath(root.right, 0)

        return self.startPath(root.left, remainingSum - root.val) + self.startPath(root.right, remainingSum - root.val)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return 0 if not root else self.startPath(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
