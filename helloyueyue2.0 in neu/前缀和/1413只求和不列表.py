class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        #找到最小前缀和min_val，output = 1 - min_val
        n = len(nums)
        min_val = float("inf")
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]
            min_val = min(min_val, prefix_sum)
        return 1 - min_val if min_val < 1 else 1