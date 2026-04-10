# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # recursive DFS
        # On time, On space
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        

        # iterative DFS - LIFO
        # On time, On space
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if node1 and node2 and node1.val == node2.val:
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left)) # first one to be popped
            elif not node1 and not node2:
                continue
            else:
                return False

        return True        
        
        # iterative BFS - FIFO
        # On time, On space
        queue = deque()
        queue.append((p,q)) # deque/array of tuples

        while queue:
            node1, node2 = queue.popleft()
            
            if p and q and p.val == q.val:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            elif not node1 and not node2:
                continue
            else:
                return False

        return True        
        