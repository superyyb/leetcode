class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        seen = {}
        left = 0
        count = 0
        n_set = set()
        n = len(nums)
        for i in range(n):
            n_set.add(nums[i])
        total = len(n_set)
        for right, x in enumerate(nums):
            seen[x] = seen.get(x, 0) + 1
            while len(seen) == total:
                count += n - right
                seen[nums[left]] -= 1
                if seen[nums[left]] == 0:
                    del seen[nums[left]]
                left += 1
        return count