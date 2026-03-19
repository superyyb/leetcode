#用heap
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        top_k = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
        for i in range(k):
            top_k.append(heapq.heappop(heap))
        indices = sorted(idx for (_, idx) in top_k)
        return [nums[i] for i in indices]

#用hash/Counter
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        top_k = sorted(nums, reverse = True)[ :k]
        need = Counter(top_k)
        res = []
        for num in nums:
            if need[num] > 0:
                res.append(num)
                need[num] -= 1
                if need[num] == 0:
                    del need[num]
                if len(need) == 0:
                    return res

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        top_k = sorted(nums, reverse = True)[ :k]
        need = Counter(top_k)
        res = []
        for num in nums:
            if need[num] > 0:
                res.append(num)
                need[num] -= 1
            if len(res) == k:
                return res