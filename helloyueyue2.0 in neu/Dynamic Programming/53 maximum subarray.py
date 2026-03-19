class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        1.dp[i]: The largest sum which ends by nums[i]
        2.Formula(How to reach dp[i]):
            If there exists dp[i-1]:
            dp[i-1] < 0: dp[i] = nums[i]
            dp[i-1] >= 0: dp[i] += dp[i - 1]
        3.Intialize dp[0] = nums[0]
        4.Travseral order:From start to end
        '''
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
                if dp[i - 1] < 0:
                    dp[i] = nums[i]
                else:
                    dp[i] = dp[i - 1] + nums[i]
        return max(dp)
