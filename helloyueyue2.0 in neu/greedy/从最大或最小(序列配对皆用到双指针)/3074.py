class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        s = sum(apple)
        for i, cap in enumerate(capacity[::-1]):
            if s - cap <= 0:
                return i + 1
            else:
                s -= cap
        """
        局部最优：每一步都选当前容量最大的箱子来尽可能多装苹果
        全局最优：直到所有苹果都能放下。
        """

class Solution: #prefixSum + BinarySearch
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        rev_capacity = sorted(capacity, reverse=True) #sorted(capacity)[::-1]
        s = sum(apple)
        n = len(capacity)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + rev_capacity[i]
        l, r = 1, n
        while l <= r:
            mid = r + (l - r) // 2
            if prefixSum[mid] < s:
                l = mid + 1
            if prefixSum[mid] >= s:
                r = mid - 1
        return l