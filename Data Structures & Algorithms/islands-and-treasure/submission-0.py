class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    # contains only the gates/treasure chests

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        # left, right, down, up

        while queue:
            r, c = queue.popleft()
            # r and c are positions of gates/treasure chests which are 0

            for dr, dc in directions:
                if 0 <= dr + r < len(grid) and 0 <= dc + c < len(grid[0]) and grid[dr+r][dc+c] == 2147483647:
                    # check if cell is infinity and not out of bounds
                    grid[dr+r][dc+c] = grid[r][c] + 1
                    # if neighbor is infinity replace with +1
                    queue.append((dr+r, dc+c))
                    # add the neighbor to the queue for the same process to take place





