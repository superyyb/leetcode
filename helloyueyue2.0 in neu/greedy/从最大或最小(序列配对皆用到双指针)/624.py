class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        distance = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for array in arrays[1:]:
            distance = max(distance, max_val - array[0])
            distance = max(distance, array[-1] - min_val)
            min_val = min(min_val, array[0])
            max_val = max(max_val, array[-1])
        return distance
    """
    避免取到同一个数组：
    每次只拿当前数组的极值与历史数组做比较，算出当前最大距离（贪心）
    再把当前数组的极值更新到历史数组中
    """

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1, min2 = float('inf'), float('inf')
        idx_min1, idx_min2 = -1, -1
        max1, max2 = float('-inf'), float('-inf')
        idx_max1, idx_max2 = -1, -1
        #遍历所有子数组，维护「最小的两个头」和「最大的两个尾」
        for i, arr in enumerate(arrays):
            head, tail = arr[0], arr[-1]
            if head < min1:
                # 新的最小 head 来了，原 min1 变成 min2
                min2, idx_min2 = min1, idx_min1
                min1, idx_min1 = head, i
            elif head < min2:
                # 只是 beat 了第二小
                min2, idx_min2 = head, i

            if tail > max1:
                # 新的最大 tail 来了，原 max1 变成 max2
                max2, idx_max2 = max1, idx_max1
                max1, idx_max1 = tail, i
            elif tail > max2:
                # 只是 beat 了第二大
                max2, idx_max2 = tail, i
        # 3) 如果最小 head 和最大 tail 来自不同数组，直接用它们
        if idx_min1 != idx_max1:
            return max1 - min1
        # 4) 否则，就只能用次优解：要么 max1–min2，要么 max2–min1
        return max(max1 - min2, max2 - min1)