class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    continue

                path.append(num)

                # Same i because we can reuse the number
                backtrack(i, remaining - num, path)

                # Undo the choice
                path.pop()

        backtrack(0, target, [])
        return result
        