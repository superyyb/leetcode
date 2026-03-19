class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        #k的选取顺序，从 max happiness开始，后面第i轮每选一个happiness[i]
        # 要减去i(前提是happiness[i] - i > 0)
        happiness = sorted(happiness, reverse = True)
        total = 0
        i = 0
        while k > 0:
            if happiness[i] - i > 0:
                total += happiness[i] - i
            # else: 思路是这个，写法上就可以省略了
            #     total += 0
            k -= 1
            i += 1
        return total

#heapq
import heapq
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        total = 0
        for happy in happiness:
            heapq.heappush(heap, - happy)#[-42, -12, -1]
        i = 0
        while heap and i < k:
            happy = heapq.heappop(heap)
            if - happy - i > 0:
                total += - happy - i
            i += 1
        return total

#heapq优秀写法
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        for i in range(len(happiness)): happiness[i] = -happiness[i]
        heapq.heapify(happiness)
        res = 0
        for i in range(k): #简洁优雅
            res += max(0, -heapq.heappop(happiness) - i)
        return res