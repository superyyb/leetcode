#Feb 23 复盘
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        algo: sliding window with fixed length
        for loop:
            expand
            shrink to valid window
            update
        '''
        left = 0
        max_average = float('-inf')
        curr_val = 0
        for right, num in enumerate(nums):
            curr_val += num
            while right - left + 1 > k:
                curr_val -= nums[left]
                left += 1
            if right - left + 1 == k:
                max_average = max(max_average, curr_val / k)
        return max_average


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    #定长窗口：每扩必缩，记录max_sum
        max_sum = float("-inf")
        curr_sum = 0
        left = 0
        n = len(nums)
        for right in range(n):
            curr_sum += nums[right]
            if right - left + 1 > k:# 先保证窗口长度 ≤ n
                curr_sum -= nums[left]
                left += 1
            if right - left + 1 == k:# 再在长度 == n 时比较
                max_sum = max(max_sum, curr_sum)
        return max_sum/k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = curr_sum = 0
        n = len(nums)
        for i, x in enumerate(nums):
            # 1. 进入窗口：加上新元素
            curr_sum += x
            # 2. 窗口尚未达到 k 时，继续扩
            if i < k - 1:
                continue
            # 3. 窗口正好是 k，更新最大和
            if curr_sum > ans:
                ans = curr_sum
            # 4. 离开窗口：减去最左侧元素
            curr_sum -= nums[i - k + 1]
        # 最后返回最大平均值
        return ans / k
"""
所以， if curr_sum > ans: 这一行之所以能保证「此时窗口长度正好是 k」，
完全是由前面的if i < k - 1: continue和紧接着减去 nums[i-k+1] 共同约束出来的。
只要 i >= k-1，我们就一直处于一个满了 k 个元素的窗口里
"""
