class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs - O(n*m*4^L) time with L = length of word, O(L) space
        # can move in any four directions, and we unmarked previously visited cells if no path found

        def dfs(r,c,word_idx):
            # base case
            if word_idx == len(word):
                return True
            
            # out of bounds, already visited, not correct letter
            if r < 0 or r > len(board) - 1 or c < 0 or c > len(board[0]) - 1 or board[r][c] == "#" or board[r][c] != word[word_idx]:
                return False

            # mark cell as visited
            original = board[r][c]
            board[r][c] = "#"
            result = dfs(r+1,c,word_idx+1) or dfs(r-1,c,word_idx+1) or dfs(r,c+1,word_idx+1) or dfs(r,c-1,word_idx+1)
            board[r][c] = original
            return result

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True

        return False
