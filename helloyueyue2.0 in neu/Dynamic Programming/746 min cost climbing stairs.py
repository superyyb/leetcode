class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        #dp[i] 是跳到第 i 级台阶并从这一级跳出去的总开销。
        dp = [0] * (n)#楼顶是dp[n - 1]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])
    """
楼顶在第 n 阶，不属于 cost 范围内
所以最后一步要 从第 n-1 或 n-2 台阶跳上去，取两者的最小花费
⇒ return min(dp[-1], dp[-2])
     """

#更直观：dp[i] 表示到第 i 层已经花费的总成本
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i]: min cost of reaching i th floor
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
    """
这种写法，dp[0]和dp[1]一开始就是0，因为站在地面（第 0 阶） ⇒ dp[0] = 0
跨一步到第 1 阶，只能从第 0 阶上来 ⇒ 也是 0 成本起跳（cost 在你踩到那阶时才付）⇒ dp[1] = 0
    """

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        a = dp[i - 2]
        b = dp[i - 1]
        新的 a ← 旧的 b（dp[i - 1]）
		新的 b ← min(a, b) + cost[i]（dp[i]）
        """
        a = cost[0]
        b = cost[1]
        n = len(cost)
        if n < 3:
            return min(a, b)
        for i in range(2, n):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)