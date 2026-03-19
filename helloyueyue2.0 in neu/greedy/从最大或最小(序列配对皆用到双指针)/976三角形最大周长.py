class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)#或者nums.sort(reverse=True)
        i = 0
        while i < len(nums) - 2:
            if nums[i] >= nums[i + 1] + nums[i + 2]:
                i += 1
            else:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0