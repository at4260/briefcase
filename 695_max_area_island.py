class Solution:
    # dfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # O(n*m) space and time
        maxArea = 0
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1


        # figure out the borders of the island
        def dfs(r, c):
            # base case
            if r < 0 or r > maxRow or c < 0 or c > maxCol or grid[r][c] == "X" or grid[r][c] == 0:
                return 0

            # mark our island
            grid[r][c] = "X"

            # initialize area and recursively visit 4 directions
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)


        # look for islands
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    islandArea = dfs(row, col)
                    maxArea = max(maxArea, islandArea)


        return maxArea
    
    # bfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # O(n*m) space and time
        island_queue = deque()
        max_area = 0
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = 1
                    grid[row][col] = "X"
                    island_queue.append((row, col))

                    while island_queue:
                        (cell_row, cell_col) = island_queue.popleft()
                        for (row_offset, col_offset) in directions:
                            nr = cell_row + row_offset
                            nc = cell_col + col_offset

                            # base case
                            if nr < 0 or nr > len(grid) - 1 or nc < 0 or nc > len(grid[0]) - 1 or grid[nr][nc] == "X" or grid[nr][nc] == 0:
                                continue

                            grid[nr][nc] = "X"
                            area += 1
                            island_queue.append((nr, nc))

                    max_area = max(max_area, area)

        return max_area    
    