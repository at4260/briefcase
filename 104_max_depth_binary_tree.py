# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive is better for balanced tree -> O(log n) space
        # bfs iterative is better for skewed -> O(1) space

        # recursive: O(n) time, O(h) space for recursion stack
        if not root:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)

        # bfs iterative: O(n) time, O(n) space for deque
        if not root:
            return 0
        
        maxDepth = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            maxDepth += 1

        return maxDepth
    