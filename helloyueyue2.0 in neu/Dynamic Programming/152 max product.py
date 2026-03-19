class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = minP = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxP, minP = minP, maxP  # 负号翻转
            maxP = max(nums[i], maxP * nums[i])
            minP = min(nums[i], minP * nums[i])
            res = max(res, maxP)
        return res