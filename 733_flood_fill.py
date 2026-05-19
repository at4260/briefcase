class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

		# DFS recurive - O(n*m) space, O(n*m) time
        def dfs(image, sr, sc, origColor, newColor):
            #base case
            if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] != origColor or image[sr][sc] == newColor:
                return
            # change color
            image[sr][sc] = newColor

            dfs(image, sr, sc+1, origColor, newColor)
            dfs(image, sr, sc-1, origColor, newColor)
            dfs(image, sr+1, sc, origColor, newColor)
            dfs(image, sr-1, sc, origColor, newColor)


        dfs(image, sr, sc, image[sr][sc], color)
        return image
    