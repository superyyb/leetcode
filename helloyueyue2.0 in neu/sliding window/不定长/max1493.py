class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        向右扩：窗口里最多只有一个0
        缩左边界：zero_count > 1时缩边，如果nums[left] 刚好为0，zero_count -= 1
        更新答案
        """
    # to maintain a subarray that has 1 zero at most
    # if zero_count > 1, move left bound until zero_count <= 1
        n = len(nums)
        zero_count = 0
        max_len = 0
        left = 0  # left bound
        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # 应当每次循环都右移left，并在移出的是 0 时把 zero_count 减一
            max_len = max(max_len, right - left)  # 因为要删掉一个，不管有没有0
        return max_len


"""
两种极端情况：是因为你在最后统一做了 return max_ans - 1，
滑动窗口的逻辑已经「隐式」涵盖了这两种极端情况：
	1.	全是 1
		由于从不遇到第二个 0，count 永远 ≤ 1，窗口会一直扩到
	    ans = right−left+1 = n，最终 max_ans = n。
		max_ans - 1 = n - 1，正好等价于「删掉一个元素之后，最长的全 1 子数组长度」的要求。
	2.	全是 0
		每次遇到一个 0，就先把它当成「窗口里唯一的那个 0」；
		但遇到第二个 0 时又立刻收缩到只剩一个 0，窗口最大长度始终是 1。
		所以 max_ans = 1，max_ans - 1 = 0
"""