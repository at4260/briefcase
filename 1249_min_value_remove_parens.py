class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # O(n) time, O(n) space

        # new_str += char is O(n^2) operation
        # better to use list and then join

        # test cases:
            # (()())
            # ))((
            # ))((ab
            # ()ab(
        
        stack = [] # indices of open parens
        new_str = list(s)
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    new_str[i] = ""

        # if anything is left in stack, that means there's an orphaned open parens
        for i in stack:
            new_str[i] = ""

        return "".join(new_str)
