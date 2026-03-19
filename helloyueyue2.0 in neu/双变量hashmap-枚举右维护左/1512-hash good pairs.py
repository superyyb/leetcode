class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        hint:If a number appears n times,
        then n * (n – 1) // 2 good pairs can be
        made  with this number.
        """
        seen = {}
        ans = 0
        for i, num in enumerate(nums):
            seen[num] = seen.get(num, 0) + 1
        for c in seen.values():
            ans += c * (c - 1) // 2
        return ans

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        ans = 0
        for num in nums:
            # num 之前出现过 counts[num] 次，那就有 counts[num] 个新的好数对
            ans += counts.get(num, 0)
            # 然后把这次出现也记入 counts
            counts[num] = counts.get(num, 0) + 1
        return ans

#或者用Counter()
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for c in cnt.values():
            ans += c * (c - 1) // 2
        return ans