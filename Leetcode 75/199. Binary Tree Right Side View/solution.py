# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        travelList = [root]

        while travelList:
            for i in range(len(travelList)):
                node = travelList.pop(0)
                if i == 0:
                    result.append(node.val)
                if node.right:
                    travelList.append(node.right)
                if node.left:
                    travelList.append(node.left)

        return result
