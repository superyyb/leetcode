class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        #定义PrefixSum
        PrefixSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            PrefixSum[i + 1] = PrefixSum[i] + nums[i]
        res = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            res += PrefixSum[i + 1] - PrefixSum[start]
        return res