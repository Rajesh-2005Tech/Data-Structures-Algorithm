class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(s, open, close):
            # If the string is complete
            if len(s) == 2 * n:
                result.append(s)
                return

            # Add '(' if we still have opening brackets
            if open < n:
                backtrack(s + "(", open + 1, close)

            # Add ')' only if it won't make the string invalid
            if close < open:
                backtrack(s + ")", open, close + 1)

        backtrack("", 0, 0)
        return result