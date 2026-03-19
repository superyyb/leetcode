class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1`# XOR operation:将nums[i]在0或1之间翻转
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1
        return count if (nums[n - 2] == 1 and nums[n - 1] == 1) \
            else -1 #check if the last two elements are both 1