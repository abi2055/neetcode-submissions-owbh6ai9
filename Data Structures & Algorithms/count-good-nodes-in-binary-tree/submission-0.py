# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs and only add to the count if previous node is greater 
        # it would be tracked inside the stack implicitly 

        def dfs(node, max_value):
            if not node:
                return 0

            if node.val >= max_value:
                result = 1
            else: 
                result = 0

            max_value = max(max_value, node.val)
            
            result += dfs(node.left, max_value)
            result += dfs(node.right, max_value)
            
            return result

        return dfs(root, root.val) 