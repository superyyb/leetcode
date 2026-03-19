class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #找到所有presum中的绝对值最大值
        presum = 0
        max_presum = 0
        min_presum = 0
        for n in nums: #前缀和不一定要套公式列表 灵活运用
            presum += n
            max_presum = max(max_presum, presum)
            min_presum = min(min_presum, presum)
        return max_presum - min_presum