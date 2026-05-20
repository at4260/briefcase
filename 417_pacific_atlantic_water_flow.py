class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # brute force O(n*m)^2 time 
        # visit every cell and then do dfs/bfs on each cell to see if it can get to both oceans

        # dfs O(n*m) time and space
        # start from the oceans and use bfs/dfs to get all cells that are assessible from each ocean
        # overlap the accessible cells from both oceans together to get the final output
        
        results = []
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r, c, prevHeight, ocean_set):
            if r < 0 or r > len(heights) - 1 or c < 0 or c > len(heights[0]) - 1 or heights[r][c] < prevHeight:    
                return

            if (r,c) in ocean_set:
                return
            ocean_set.add((r, c))
            dfs(r+1, c, heights[r][c], ocean_set)
            dfs(r-1, c, heights[r][c], ocean_set)
            dfs(r, c+1, heights[r][c], ocean_set)
            dfs(r, c-1, heights[r][c], ocean_set)

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) not in pacific_visited and (row == 0 or col == 0):
                    dfs(row, col, heights[row][col], pacific_visited)
                if (row, col) not in atlantic_visited and (row == len(heights) - 1 or col == len(heights[0]) - 1):
                    dfs(row, col, heights[row][col], atlantic_visited)
                

        return list(set(pacific_visited).intersection(atlantic_visited))
