class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s = sum(nums[:k])
        max_sum = s
        for i in range(k,len(nums)):
            s = s + nums[i]-nums[i-k]
            max_sum = max(max_sum , s)
        return max_sum/k        