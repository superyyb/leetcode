#较复杂
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        n = len(cost)
        i = 0
        total = 0
        if n < 2:#处理不足3件的边界情况
            return sum(cost)
        while i < n - 1:
            total += cost[i] + cost[i + 1]
            i += 3
            if n - i < 3:
                total += sum(cost[i : n])
                break
        return total

#取模 简单易读
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for idx, c in enumerate(cost):
            if idx % 3 != 2:#只有idx % 3 == 2 的那件免费
                total += c
        return total