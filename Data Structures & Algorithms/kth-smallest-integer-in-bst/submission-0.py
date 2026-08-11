# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # stack = [root]
        # visited = set()

        # while stack:
        #     node = stack.pop()

        #     if node in visited:
        #         continue
        #         # skip this loop
            
        #     visited.add(node)

        #     if node.left and node.left not in visited:
        #         stack.append(node.left)
            
        #     if node.right and node.right not in visited:
        #         stack.append(node.right)

        # print([node.val for node in visited])

        # return 0

        # no cycle detection required not a graph, visited not required

        count = 0
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                # go all the way down left adding to the stack
                # you could go right as well
                current = current.left

            current = stack.pop()
            count += 1
            if count == k:
                # always has atleast k elements
                return current.val
            
            current = current.right

        return current.val
            

