class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # O(n*m) time, O(n*m) space
        # max height must be <= max value in vertical and horitizontal

        # create row max
        # row 0 max = 8
        # row 1 max = 7
        # row 2 max = 9
        # row 3 max = 3
        # [8,7,9,3]

        # create col max
        # col 0 max = 9
        # col 1 max = 4
        # col 2 max = 8
        # col 3 max = 7
        # [9,4,8,7]

        # use coordinate to get the min of the row max and col max
        # r0c0 = min(8, 9) => 8
        # r0c1 = min(8, 4) => 4
        # r2c3 = min(7, 9) => 7

        # transposing is flipping r and c vals
        # 0,0=>0,0
        # 0,1=>1,0
        # 0,2=>2,0
        # 2,3=>3,2
        # [[0] * len(grid)] * len(grid[0]) creates references to the same inner array
        # "*"" repeats references so only works if repeated val is immutable
        transposed_grid = [[0] * len(grid) for i in range(len(grid[0]))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                transposed_grid[c][r] = grid[r][c]

        rows_max = []
        for r in range(len(grid)):
            rows_max.append(max(grid[r]))

        cols_max = []
        for r in range(len(transposed_grid)):
            cols_max.append(max(transposed_grid[r]))
            
        diff_total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curr = grid[r][c]
                new = min(rows_max[r], cols_max[c])
                diff_total += new - curr

        return diff_total


        # slightly better, skips the transposed grid
        # build row max and col max in one pass, row max is direct, col max is calc by accumulating
        rows_max = [0] * len(grid)
        cols_max = [0] * len(grid[0])
        for r in range(len(grid)):
            rows_max[r] = max(grid[r])
            for c in range(len(grid[0])):
                cols_max[c] = max(cols_max[c], grid[r][c])

        diff_total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curr = grid[r][c]
                new = min(rows_max[r], cols_max[c])
                diff_total += new - curr

        return diff_total    
    