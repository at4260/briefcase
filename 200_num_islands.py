class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # only ever gets called when we hit a "1"
        def dfs(r, c):
            # base case
            if r < 0 or r > maxRow or c < 0 or c > maxCol or grid[r][c] == "X" or grid[r][c] == "0":
                return

            # mark it
            grid[r][c] = "X"

            # go find all the other 1s nearby to mark as part of this island
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            

        islands = 0
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands        

