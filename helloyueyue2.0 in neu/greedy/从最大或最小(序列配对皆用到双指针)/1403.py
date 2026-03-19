class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        #从大到小排序，找到num相加大于sum(nums)一半的list
        nums = sorted(nums, reverse = True) #[10,9,8,4,3]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total > sum(nums) * 0.5:
                return nums[ : i + 1]
