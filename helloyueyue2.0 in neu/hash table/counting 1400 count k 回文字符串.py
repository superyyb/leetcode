from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        count = 0
        dic = {}
        S = Counter(s)
        for key, value in S.items():
            if value % 2 != 0:
                count += 1
        if count <= k:
            return True
        return False