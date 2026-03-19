class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = {}
        max_res = -1
        for num in nums:
            val = 0
            for n in map(int, str(num)):
                val += n
            if val in seen:
                res = num + seen[val]
                max_res = max(res, max_res)
                seen[val] = max(num, seen[val])#这一步很关键：有可能新来的num比之前储存的更大
            else:
                seen[val] = num
        return max_res