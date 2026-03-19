class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        seen = {}
        for char in list(s):
            seen[char] = seen.get(char, 0) + 1
        if len(seen) <= k:
            return 0
        else:
       #按 value 升序排列所有键 #{'a': 3, 'b': 4, 'c': 1}
            counts = sorted(seen.values())#[1,3,4]
            return sum(counts[:(len(seen) - k)])

from collections import Counter
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        seen = Counter(s)
        if len(seen) <= k:
            return 0
        else:
       #按 value 升序排列所有键 #{'a': 3, 'b': 4, 'c': 1}
            counts = sorted(seen.values())#[1,3,4]
            return sum(counts[:(len(seen) - k)])