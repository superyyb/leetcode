#最优解 heap O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #nums = [1,1,1,2,2,3] freq = {1:3, 2:2, 3:1}
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)#heappop永远是最小值
        res = []
        for i in range(k):
            freq[num], num = heapq.heappop(heap)
            res.append(num)
        return res
    """
    Python 默认是 最小堆，会根据元素的顺序可比性决定堆顶。
    如果堆里是 二元组 (a, b)：
1.	先比较第一个元素 a；
2.	如果相等，再比较第二个元素 b。
所以 (count[num], num) 会 优先按频率 count[num] 排序，
    """


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return heapq.nlargest(k, freq.keys(), key=freq.get)

#bucket sort
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        bucket = [[] for _ in range(len(nums) + 1)]  # 一定设成[]，存在相同频率的数字
        for key, value in freq.items():
            bucket[value].append(key)
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


#不是最优解 time: T(n)=O(N)+O(MlogM)+O(K) time: O(NlogN)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #nums = [1,1,1,2,2,3] freq = {1:3, 2:2, 3:1}
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        #直接对dic.items()进行排序，按出现次数排序，即按value排序
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_items[:k]]
    """
    lambda x: x[1]等价于def f(x): return x[1]
	•把每个元素 x 映射为 x[1] 来排序。
	•在 freq.items()里，x是一个二元组(num, count)，因此 x[1] 就是 count（出现次数）。
	•所以这行代码会“按出现次数排序”。
    """