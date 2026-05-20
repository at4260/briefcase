class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # brute force O(n*m)^2 time 
        # visit every cell and then do dfs/bfs on each cell to find treasure chest
        # alternative brute force: O(n*m)^2 time 
        # start from the treasure chest and bfs/dfs while updating each cell with the distance 
        # runs through the whole grid for each treasure chest

        # multi-source bfs O(n*m) time and space
        # track "rounds" to capture the distance. whichever one gets there first is guaranteed to be shorter distance
        # start from the treasure chests and bfs all of the chests at the same time to start updating distance

        tc_queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    tc_queue.append((row, col))

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        distance = 1
        while tc_queue:
            for i in range(len(tc_queue)):
                (cell_row, cell_col) = tc_queue.popleft()

                for (row_offset, col_offset) in directions:
                    nr = row_offset + cell_row
                    nc = col_offset + cell_col

                    if nr < 0 or nr > len(grid) - 1 or nc < 0 or nc > len(grid[0]) - 1 or grid[nr][nc] != 2147483647:
                        continue
                    # only move forward with inf values, otherwise it's a water cell, treasure chest, or assigned distance
                    grid[nr][nc] = distance
                    tc_queue.append((nr, nc))

            distance += 1

        # modify grid in place