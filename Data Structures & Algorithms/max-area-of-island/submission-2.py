class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # bfs traversal 
        # check neighbors each iteration 
        # when all surrounding adjacent neighbors (not diagonal) are 0
        # update the count

        # this will represents all the nodes visited as a global var
        visited = set()
        count = 0
        max_area = 0

        def bfs(row, column):
            queue = collections.deque()
            queue.append((row, column))
            visited.add((row, column))
            count = 1

            while queue:
                row, column = queue.popleft()

                # must check each direction for bfs for adjacent nodes
                directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

                # loop through the directions
                for drow, dcol in directions:
                    # checks 
                    if (0 <= row + drow < len(grid) and 
                        0 <= column + dcol < len(grid[0]) and 
                            grid[row + drow][column + dcol] == 1 and
                                (row + drow, column + dcol) not in visited):
                                    queue.append((row + drow, column + dcol))
                                    visited.add((row + drow, column + dcol))
                                    count += 1
            return count
                    

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                # only bfs is a 1 ignore all the 0s
                if grid[row][col] == 1 and (row, col) not in visited:
                    # basically performing bfs on the graph node
                    count = bfs(row, col)

                max_area = max(max_area, count)
                count = 0
                
        return max_area