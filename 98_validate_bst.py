# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # at given node, left node < node and right node > node (passing down a min, max)
        # if not, return False
        # if so, go down both left and right nodes

        # O(n) time
        # O(h) space

        def isValidNode(node, minVal, maxVal) -> bool:
            if not node:
                return True
            if not minVal < node.val < maxVal:
                return False
            return isValidNode(node.left, minVal, node.val) and isValidNode(node.right, node.val, maxVal)

        return isValidNode(root, minVal=float('-inf'), maxVal=float('inf'))
    