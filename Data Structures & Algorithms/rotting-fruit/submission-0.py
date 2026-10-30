class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = collections.deque()
        
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh_count += 1
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while queue and fresh_count > 0:
            # from a fresh rotten banana you want to go in every direction
            for i in range(len(queue)):
                # there can be multiple rotten bananas in the queue
                r, c = queue.popleft()

                for dc, dr in directions:
                    row = r + dr
                    col = c + dc
                    if (row < rows and row >= 0 and col < cols and col >= 0 and grid[row][col] == 1): 
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh_count -= 1
                        # append the new rotten bananas to the list
            time += 1

        if fresh_count == 0:
            return time
        else:
            return -1





        