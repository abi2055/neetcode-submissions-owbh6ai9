# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # edge cases 

        # have a running count of left and right
        # if left and right differ by max 1 then return true
        self.balanced = True

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(right - left) > 1:
                self.balanced = False

            return 1 + max(left, right)

        dfs(root)

        return self.balanced