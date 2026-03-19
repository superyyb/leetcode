class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
    output: min nubmers of operations
    -> max length of continuous subarray(whose sum equals to total - x)
        """
        n = len(nums)
        left = 0
        curr_sum = 0
        max_ans = -1
        ans = 0
        total = 0
        for i in range(n):
            total += nums[i]
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum > total - x and left <= right:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == total - x:
                ans = right - left + 1
                max_ans = max(max_ans, ans)
        return n - max_ans if max_ans != -1 else -1
        #因为max_ans初始值设了-1，重新赋值则返回新值