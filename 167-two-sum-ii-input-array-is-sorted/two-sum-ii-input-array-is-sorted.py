class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
            s = numbers[i]+numbers[j]
            if s == target:
                return[i+1,j+1]
            elif s<target:
                i = i+1
            else:
                j = j-1

        