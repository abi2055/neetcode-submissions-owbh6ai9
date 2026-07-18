# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # a bfs algorithm would work i feel like
        # a memoization dp solution with recursion would work
        # what is the brute force 

        if root is None:
            return []

        queue = deque([root])
        output = []

        while queue:
            level_range = len(queue)
            # how many nodes in that level to append
            level_nodes = []
            # temp storage

            for _ in range(level_range):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            output.append(level_nodes)

        return output

                
                






