# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSums = []
        travelList = [root]

        while travelList:
            levelSums.append(sum(node.val for node in travelList))
            for i in range(len(travelList)):
                node = travelList.pop(0)
                if node.right:
                    travelList.append(node.right)
                if node.left:
                    travelList.append(node.left)              

        return levelSums.index(max(levelSums)) + 1
