class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # look for the first character in the word inside the list
        # from that character cant you run 2d dfs?
        # check all neighbors, if one allows 
        # then check all of its neighbors 
        # base case: not character of the word or less than 3 chars
        # if subset < 3:
        # return
        rows = len(board)
        cols = len(board[0])

        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path):
                return False
            # conditions for false
            # out of bounds on the row or the column
            # the letter in word at position i does not match the adjacent tile
            # or that tile has already been checked dfs style

            path.add((r,c))

            #backtracking logic
            result = (
                dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            )

            path.remove((r,c))

            return result

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

        

            