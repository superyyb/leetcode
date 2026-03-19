class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        1.先计算出不需要手段也satisfy的人数作为base
        2.这里的定长滑窗是minutes 从第一个minutes计算出ans（本该不satisfy，用了手段才satisfy的人数），
        3.滑动窗口更新ans，最后return ans + base
        """
        ans = curr_count = 0
        n = len(customers)
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
        for i, x in enumerate(customers):
            if grumpy[i] == 1:
                curr_count += x
            if i < minutes - 1: #扩
                continue
            ans = max(ans, curr_count) #更新
            if grumpy[i - minutes + 1] == 1: #缩
                curr_count -= customers[i - minutes + 1]
        return ans + base