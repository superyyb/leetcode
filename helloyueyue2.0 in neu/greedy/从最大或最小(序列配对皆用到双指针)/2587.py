class Solution:
    def maxScore(self, nums: List[int]) -> int:
        count = 0
        prefixSum = 0
        nums = sorted(nums, reverse = True)
        for num in nums:
            prefixSum += num
            if prefixSum > 0:
                count += 1
        return count