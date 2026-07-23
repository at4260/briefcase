class Solution:
    def removeDuplicates(self, s: str) -> str:

        # two pointers
        # aazz => "" (left 0, right 1 -> left 2, right (left + 1)
        # abzzba => "" (left 0, right 1, left 1, right 2, left 2, right 3, => 
            # left 1, right 5)
        # abbaca => "ca"
        
        # stack
        # aazz => if empty, a; pop a == a? leave pop; z, add to stack, 
        # abzzba => if empty, a; pop a == b? ab; pop b? b == z? no, add z, pop z? z == z? leave pop
        # abbaca => 
        
        # O(n) time, O(n) space
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                last_char = stack.pop()
                if last_char != char:
                    stack.append(last_char)
                    stack.append(char)
                    
        return "".join(stack)        
    