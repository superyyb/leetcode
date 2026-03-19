class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        #符合条件的array nums[i+1] - nums[i]肯定为奇数
        for i in range(1, len(nums)):
            if (nums[i] - nums[i - 1]) % 2 == 0:#取余
                return False
        return True