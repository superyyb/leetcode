#prefixsum
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

#不需要额外的space给prefixsum，直接用sum减去每个num即可
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        _sum = sum(nums)
        n = len(nums)
        for i in range(n - 1, 1, -1):
            _sum -= nums[i]
            if _sum > nums[i]:
                return _sum + nums[i]
        return -1
