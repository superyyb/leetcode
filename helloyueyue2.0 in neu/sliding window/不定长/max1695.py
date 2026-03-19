#Feb23 复盘
from collections import Counter
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
        sliding window
        Not the longest/shortest, the biggest value
        扩
        while 缩
        update
        '''
        left = 0
        max_val, curr_val = 0, 0
        num_freq = Counter()
        for right, num in enumerate(nums):
            curr_val += num
            num_freq[num] += 1
            while num_freq[num] > 1:
                num_freq[nums[left]] -= 1
                curr_val -= nums[left]
                if num_freq[nums[left]] == 0:
                    del num_freq[nums[left]]
                left += 1
            max_val = max(max_val, curr_val)
        return max_val

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        得到和最大的不重复数字的连续数列
        total 应该反映当前滑动窗口里所有元素的和，不论它们是不是第一次出现。因此：
	1.	新元素进窗口时，无论是否重复，都要 total += x
	2.	左边界收缩时，移除元素一定要 total -= nums[left]
        """
        seen = {}
        left = 0
        max_total = total = 0
        n = len(nums)
        for right, x in enumerate(nums):
            seen[x] = seen.get(x, 0) + 1 #扩
            total += x
            while seen[x] > 1: #缩
                seen[nums[left]] -= 1
                total -= nums[left]
                left += 1
            max_total = max(max_total, total) #更新
        return max_total