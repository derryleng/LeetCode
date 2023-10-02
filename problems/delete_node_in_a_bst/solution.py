# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# 1. Search for a node to remove.
# 2. If the node is found, delete the node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val == key:
                if root.right:
                    newRoot = root.right

                    # Append left tree to smallest node on right tree
                    while newRoot.left:
                        newRoot = newRoot.left
                    newRoot.left = root.left
                    return root.right
                else:
                    return root.left
            elif root.left and root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.right and root.val < key:
                root.right = self.deleteNode(root.right, key)

        return root
