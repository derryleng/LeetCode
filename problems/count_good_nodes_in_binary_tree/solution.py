# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: TreeNode, val: int) -> int:
        if not root:
            return 0

        if root.val >= val:
            return 1 + self.traverse(root.left, root.val) + self.traverse(root.right, root.val)

        return self.traverse(root.left, val) + self.traverse(root.right, val)

    def goodNodes(self, root: TreeNode) -> int:
        return 0 if not root else self.traverse(root, -inf)
