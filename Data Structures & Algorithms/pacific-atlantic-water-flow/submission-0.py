class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # literally if all adjacent cells are smaller than the current cell then the flow can happen 
        # up and left is always pacific from a cell
        # down and right is always atlantic from a cell 
        # dfs problem

        pacific = set()
        atlantic = set()
        # we're gping to join thse two sets

        cols = len(heights[0])
        rows = len(heights)

        def dfs(r, c, visited, prevH):
        # row, col, visited set, prevH
            if ((r,c) in visited or r < 0 or c < 0 or c == cols or r == rows or heights[r][c] < prevH):
                return
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            # top edge
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
            # bottom edge

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            # left edge
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
            # right edge

        results = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    results.append([r,c])

        return results
        
