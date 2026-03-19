class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for row, lim in zip(grid, limits):
            row.sort(reverse=True)
            candidates.extend(row[:lim])  # 只取每行最大的lim 个
        candidates.sort(reverse=True)
        return sum(candidates[:k])  # 全局排序，取前 k

    """
    zip()将多个可迭代对象（list, tuple, str等）“压缩”成一个个元组
    """
#用heap
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for row, lim in zip(grid, limits):
            row.sort(reverse = True)
            for i in range(lim):
                heapq.heappush(heap, -row[i])
        res = 0
        for i in range(k):
            res += - heapq.heappop(heap)
        return res
