# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs iterative
        # O(n) time, O(w) space (in balanced tree, it's O(n/2) -> O(n) representing nodes in the last layer)
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
    

        # dfs recursive - save each level the node belongs to
        # O(n) time, O(h) space excluding output for the call stack, O(n) total
        res = []
        def dfs(node, level):
            if not node:
                return 
            
            # if new level, create array
            if level == len(res):
                res.append([])

            # add current node to the subarray corresponding to its level
            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
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
