class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # O(n*m) time, O(n*m) space (dict with 2^m / 2 size tuple keys)

        matrix_map = defaultdict(int) # {(0,0,0): 1, (0,0,1): 2}
        for row in matrix:
            # standardize with 0 as first digit -> 001, 110 => all map to 001
            # to avoid checking/storing 0,1 and 1,0 in dict
            if row[0] == 1:
                row = [1 if val == 0 else 0 for val in row ]    
            matrix_map[tuple(row)] += 1  # key must be immutable
            
        return max(matrix_map.values())
    