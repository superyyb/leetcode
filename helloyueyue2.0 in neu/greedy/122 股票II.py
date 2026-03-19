class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        diff = [0] * (len(prices) - 1)
        for i in range(len(prices) - 1):
            diff[i] = prices[i + 1] - prices[i]
        for d in diff:
            if d > 0:
                profit += d
        return profit

    """
    把整体利润拆为每天的利润,只收集每天的正利润
    prices[3] - prices[0]相当于(prices[3] - prices[2]) + (prices[2] - prices[1]) + (prices[1] - prices[0])。
    """