class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        """
        k是窗口长度
        当窗口里不同元素(distinct) >= m 时，更新最大sum。
        """
        n = len(nums)
        seen = {}
        ans = sum = 0 #包含base case：If no such subarray exists, return 0.
        distinct = 0
        for i, x in enumerate(nums):
            sum += x
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1
            if seen[x] == 1:
                distinct += 1
            if i < k - 1: #扩
                continue
            if distinct >= m: #检查更新
                ans = max(ans, sum)
            sum -= nums[i - k + 1] #缩
            seen[nums[i - k + 1]] -= 1
            if seen[nums[i - k + 1]] == 0:
                del seen[nums[i - k + 1]]
                distinct -= 1
        return ans