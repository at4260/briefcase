# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs iterative
        # O(n) time, O(n) space (actually O(n/2) queue can hold all nodes in last level which is approx half the nodes of the tree)
        queue = deque()
        if root:
            queue.append(root) 

        res = []
        level = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            level = []
            
        return res
    

# print all nodes in a binary tree
class Solution:
    def printNodes(self, root: Optional[TreeNode]) -> None:
        # dfs recursive
        # O(n) time, O(h) space (precise)
            # if balanced tree (best case) -> O(log n) space; if skewed tree (worst case) -> O(n) space
        
        if not root:
            return
        print(root.val)
        self.printNodes(root.left)
        self.printNodes(root.right)
