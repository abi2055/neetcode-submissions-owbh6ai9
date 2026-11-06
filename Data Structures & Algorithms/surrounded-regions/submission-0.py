class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # anything on the border would not be surrounded
        # anything touching that o would also not be surrounded
        # so that's what needs to be checked

        rows = len(board)
        cols = len(board[0])

        def transform(r, c):
            # base case
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return 
            board[r][c] = "T"

            # different directions
            transform(r - 1, c)
            transform(r + 1, c)
            transform(r, c - 1)
            transform(r, c + 1)

        # convert unsurrounded areas
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and r in [rows - 1, 0] or c in [cols - 1, 0]:
                    transform(r, c)

        # convert surounded areas 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # convert unsurrounded areas back 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"










