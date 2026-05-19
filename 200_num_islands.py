class Solution:
    # dfs
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(n*m) time and space (call stack)
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

        # bfs - once we find a "1", search for the rest of the island
        def numIslands(self, grid: List[List[str]]) -> int:
            # O(n*m) time and space (queue)
            islands_queue = deque()
            islands = 0
            directions = [(1,0), (-1, 0), (0, -1), (0, 1)]

            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == "1":
                        islands += 1
                        grid[row][col] = "X"
                        islands_queue.append((row, col))

                        while islands_queue:
                            (cell_row, cell_col) = islands_queue.popleft()
                            for (row_offset, col_offset) in directions:
                                nr = cell_row + row_offset
                                nc = cell_col + col_offset
                                if nr < 0 or nr > len(grid) - 1 or nc < 0 or nc > len(grid[0]) - 1 or grid[nr][nc] == "0" or grid[nr][nc] == "X":
                                    continue
                                grid[nr][nc] = "X"
                                islands_queue.append((nr, nc))

            return islands
        