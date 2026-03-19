class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        #设一个哈希表，按照value排序
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        counts = sorted(freq.values(), reverse = True)
        half = len(arr)//2
        removed = 0
        for i in range(len(counts)):
            removed += counts[i]
            if removed >= half:
                return i + 1

#max_heap
import heapq
from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        构造一个“最大堆”：Python 的 heapq 是最小堆，
        所以把频次取负数，负数越小（绝对值越大）就越先被 pop
        """
        freq = {}
        heap = []
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        for cnt in freq.values():
            heapq.heappush(heap, -cnt)
        half = len(arr) // 2
        removed = 0
        sets = 0
        while removed < half:
            removed += -heapq.heappop(heap)#每次pop一个最大频次
            sets += 1
        return sets