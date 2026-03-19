class Solution:
    def minPairSum(self, nums: List[int]) -> int:
    #为了保证是minimized maximum pair sum，数列排序后首尾相加
        nums.sort()
        max_val = 0
        i, j = 0, len(nums) - 1
        while i < j:
            curr_val = nums[i] + nums[j]
            max_val = max(max_val, curr_val)
            i += 1
            j -= 1
        return max_val