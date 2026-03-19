class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]: the length of longest increasing subsequence ended with nums[i]
        #return: max(dp[i])
        #if nums[i] > nums[i - 1]:为什么不行：subsequence允许跳过数字
        #所以必须用j遍历所有在i之前的数字
        n = len(nums)
        dp = [1] * n
        #dp[0] = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

"""
nums = [2, 5, 3, 7]
计算 i=3 (nums[i]=7) 时：
	•	可以接在 2 后 → [2,7]   长度 2
	•	可以接在 5 后 → [2,5,7] 长度 3
	•	可以接在 3 后 → [2,3,7] 长度 3
因为可能有多个 j 可以连接，我们只取最长的那一条路径。
dp[3] = max(dp[0]+1, dp[1]+1, dp[2]+1) = 3
"""