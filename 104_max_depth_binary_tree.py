# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive; O(n) time, O(h) space for recursion stack
        if not root:
            return 0

        resLeft = self.maxDepth(root.left) + 1
        resRight = self.maxDepth(root.right) + 1

        return max(resLeft, resRight)

