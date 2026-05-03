# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(nodep, nodeq):
            if not nodep and not nodeq:
                return True

            if nodep is None or nodeq is None:
                return False
            
            if nodep.val != nodeq.val:
                return False
            
            return dfs(nodep.left, nodeq.left) and dfs(nodep.right, nodeq.right)

        is_same = dfs(q, p)
        return is_same
            