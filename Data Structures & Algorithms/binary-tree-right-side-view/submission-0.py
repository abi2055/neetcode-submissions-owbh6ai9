# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # the right most node of each level is what you need
        # nodes on the right side would take precedence if not null 
        # if theres none on the right side traversel check the left side
        # closest to the right 
        # use bfs to analyze this

        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = len(queue)

            for i in range(level):
                node = queue.popleft()
                if i == level - 1:
                    # last node in the queue 
                    # which would the right most
                    result.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return result
