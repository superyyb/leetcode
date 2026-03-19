#反面案例：Time O(n2) min(seen)每次都要遍历一次set
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = set()
        max_profit = 0
        for price in prices:
            seen.add(price)
            profit = price - min(seen)
            max_profit = max(max_profit, profit)
        return max_profit

#Mar5复盘
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Initialize 2 para: min_price, max_profit

        Traverse the list:
        1.Store and update the min_price
        2.Calculate current price - min_price
        3.Store and update the max_profit
        '''
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit