class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs to track a "step" at a time, O(n*m*k) time, O(n*m*k) space
        steps = 0
        visited = set() # don't mark with X since cell can get visited multiple times from diff paths
        queue = deque()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        queue.append((0,0,k))

        while queue:
            for i in range(len(queue)):
                (r, c, k_remaining) = queue.popleft()

                # if reached bottom corner, return steps
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return steps
                
                if (r,c,k_remaining) in visited:
                    continue
                visited.add((r,c,k_remaining))

                # otherwise, start bfs
                for (row_offset, col_offset) in directions:
                    nr, nc = row_offset + r, col_offset + c

                    # out of bounds
                    if nr < 0 or nc < 0 or nr > len(grid) - 1 or nc > len(grid[0]) - 1:
                        continue

                    # if obstacle, check if enough k to eliminate
                    if grid[nr][nc] == 1:
                        if k_remaining == 0:
                            continue # can't pass
                        queue.append((nr, nc, k_remaining - 1)) # add but decrement k_remaining


                    # if no obstacle, add to queue
                    elif grid[nr][nc] == 0:
                        queue.append((nr, nc, k_remaining))

            steps += 1

        return -1

# Note: There's a little bit of inefficiency with revisiting the same cell because the k value is different.
# Ex: grid [[0,1,0][0,0,0]] in round 2 at (0,1,k=0) it will try to go back to cell (0,0) but with k=0 this time                    
# and visited set only has (0,0,1), so it'll try to reprocess
