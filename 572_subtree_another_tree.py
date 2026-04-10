# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # iterative dfs
        # O(n*m) space, O(n+m) time
        if root and not subRoot:
            return True
        if subRoot and not root:
            return False

        stack = [root]
        while stack:
            node1 = stack.pop()
            if node1 and self.sameTree(node1, subRoot):
                return True
            elif not node1:
                continue
            else:
                stack.append(node1.right)
                stack.append(node1.left)

        return False


    def sameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        stack = [(t1, t2)]
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2 and node1.val == node2.val:
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
            elif not node1 and not node2:
                continue
            else:
                return False
        
        return True
    


        # recursive dfs
        # O(n*m) time, O(n+m) space
        if root and not subRoot:
            return True
        if subRoot and not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False