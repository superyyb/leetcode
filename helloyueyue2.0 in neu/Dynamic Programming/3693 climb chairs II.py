class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs#Add [0] to make it 1-index list
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if i >= 1:
                dp[i] = min(dp[i], dp[i - 1] + 1 + costs[i])
            if i >= 2:#千万不能用elif
                dp[i] = min(dp[i], dp[i - 2] + 4 + costs[i])
            if i >= 3:
                dp[i] = min(dp[i], dp[i - 3] + 9 + costs[i])
        return dp[n]