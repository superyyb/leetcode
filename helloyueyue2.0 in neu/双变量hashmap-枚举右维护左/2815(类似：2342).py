class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = {}
        max_val = -1
        for num in nums:
            n = max(map(int, str(num)))#注意map用法
            if n in seen:
                val = num + seen[n]
                max_val = max(val, max_val)
                seen[n] = max(seen[n], num)#这一步很关键：有可能新来的num比之前储存的更大
            else:
                seen[n] = num
        return max_val