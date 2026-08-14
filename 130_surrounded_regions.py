class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # start from the edges and mark anything "R" that is not a surrounded region
        # anything that didn't get touched is a surrounded region; restore "R" areas back
        
        # O(n*m) time, space (marked once for the entirety of the problem; word search revisits marked cells)
        def dfs(row, col):
            if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1 or board[row][col] in ("R", "X"):
                return

            board[row][col] = "R"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            return


        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1:
                    dfs(row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "R":
                    board[row][col] = "O"