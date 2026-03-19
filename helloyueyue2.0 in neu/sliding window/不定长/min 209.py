#Feb23复盘
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        min length of subarray: sliding window with unfixed length
        '''
        left = 0
        min_len = float('inf')
        curr_val = 0
        for right, num in enumerate(nums):
            curr_val += num
            while curr_val >= target:
                min_len = min(min_len, right - left + 1)
                curr_val -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        不定长窗口：触发条件时（sum>=s）才收缩left
        """
        n = len(nums)
        min_len = float("inf")
        left = 0
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right] #扩
            while curr_sum >= target: #更新
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1 #缩
        return 0 if min_len == float("inf") else min_len
    """
    可以存在left == right的情况，说明nums[left]一个元素就可以满足target，
    此时最短长度是right - left + 1 为 1
    """

