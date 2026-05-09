# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # once you find a potential match then go all the way down
        
        def checkSubtree(node, subNode):
            if not node and not subNode:
                return True
            # condition goes all the way to the end meaning both nodes end
            # at the same time

            if not node or not subNode:
                return False
            # goes all the way to end on one tree but not the other

            if node.val != subNode.val:
                return False
            # values do not match

            return checkSubtree(node.left, subNode.left) and checkSubtree(node.right, subNode.right)

        def search(node):
            if not node:
                return False
            # no starting point found

            if checkSubtree(node, subRoot):
                return True
            
            # found a starting point
            
            return search(node.left) or search(node.right)

        is_same = search(root)
        return is_same

