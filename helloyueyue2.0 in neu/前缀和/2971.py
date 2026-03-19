class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #prefix sum
        n = len(nums)
        if n < 3:
            return -1
        nums.sort()
        prefixsum = [0] * (n + 1)
        max_perimeter = -1
        for i in range(n):
            prefixsum[i + 1] = prefixsum[i] + nums[i]
            if prefixsum[i] * 2 > prefixsum[i + 1]:
                max_perimeter = max(max_perimeter, prefixsum[i + 1])
        return max_perimeter