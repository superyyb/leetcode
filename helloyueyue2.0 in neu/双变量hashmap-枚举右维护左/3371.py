class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        #remove the outlier from the list
        seen = {}
        max_outlier = float("-inf")
        total_sum = sum(nums)
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        for num in nums:
            outlier = total_sum - 2*num
            if outlier in seen:
                if outlier != num or seen[num] > 1:#如果 outlier 刚好和 num 一样，那么在 seen 中的计数必须 > 1
                    max_outlier = max(max_outlier, outlier)
        return max_outlier

from collections import Counter
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        cnt   = Counter(nums)
        ans   = float("-inf")
        # 按原数组顺序，把每个 num 当成候选 outlier
        for num in nums:#先 “移除”当前值
            cnt[num] -= 1
            if cnt[num] == 0:
                del cnt[num]
            rem = total - num
            # 验证偶数性和 half 是否存在
            if rem % 2 == 0 and cnt.get(rem // 2, 0) > 0:
                ans = max(ans, num)
            # 恢复 cnt，供后续元素使用
            cnt[num] = cnt.get(num, 0) + 1
        return ans