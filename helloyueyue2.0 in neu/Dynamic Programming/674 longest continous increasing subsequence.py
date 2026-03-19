#time: O(n) space:O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 1
        length = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1
        return max_length

#time: O(n) space:O(n)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
    dp[i]:the length of longest continuous subseq ended with nums[i]
    return: max(dp[i])
        """
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:#连续 → 只看 i-1
                dp[i] = dp[i - 1] + 1
        return max(dp)