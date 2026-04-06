# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # self.left, self.right = self.right, self.left
        
        if root is None:
            return 
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        # swap left and right of the children
        # go down the left branch further 
        # perform the swap on the left again
        # repeat until it is none, esentially stopping the recutsion further on the left branch 
        # when its none then it moves onto the next line which is the right branch 
        # and does the same thing as the left side 