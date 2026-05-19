class Solution:
    # bfs only solution because level-by-level processing (expanding one layer at a time)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # O(n*m) time and space
        rottenQueue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rottenQueue.append((row, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1
        minutes = 0

        while rottenQueue:
            for i in range(len(rottenQueue)): 
                (cellRow, cellCol) = rottenQueue.popleft()
                for (rowOffset, colOffset) in directions:
                    nr = cellRow + rowOffset
                    nc = cellCol + colOffset
                    if nr < 0 or nr > maxRow or nc < 0 or nc > maxCol or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue
                    # fresh orange
                    grid[nr][nc] = 2
                    rottenQueue.append((nr, nc))

            if rottenQueue: # don't increment the time when there's nothing left to spread 
                minutes += 1

        for row in grid:
            if 1 in row:
                return -1

        return minutes
