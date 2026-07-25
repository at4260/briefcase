class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # On time, O1 space
        val = 0
        for operation in operations:
            if operation in ("++X", "X++"):
                val += 1
            elif operation in ("--X", "X--"):
                val -= 1
        return val
    