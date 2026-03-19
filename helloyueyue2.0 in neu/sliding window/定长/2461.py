class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    #不能用set简单地add/remove，因为无法区分重复元素，需要用hash/dict记录重复频次
        ans = sum = 0
        seen = {}
        n = len(nums)
        for i, x in enumerate(nums):
            sum += x
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1
            if i < k - 1:
                continue #扩
            if len(seen) == k:
                ans = max(ans, sum)
            sum -= nums[i - k + 1] #缩
            seen[nums[i - k + 1]] -= 1
            if seen[nums[i - k + 1]] == 0:
                del seen[nums[i - k + 1]]
        return ans