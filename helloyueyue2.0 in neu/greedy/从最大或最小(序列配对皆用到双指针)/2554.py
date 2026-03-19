class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        banned_set = set(banned) #在循环前就转为set 只要做一次
        for i in range(1, n + 1):
            if i not in banned_set and maxSum - i >= 0:
                maxSum -= i
                count += 1
                if maxSum < i:
                    break
        return count
"""
Python 列表的 in 是O(n)操作，最坏情况下会把算法退化到 O(n²)。
进入循环前先把 banned 先转成 set，可以把每次判断降到摊销 O(1)。
"""
