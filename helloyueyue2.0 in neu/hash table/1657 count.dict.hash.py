#time: O(NlogN)  O(N) 的遍历和 O(KlogK) 的排序
from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for char in word1:
            freq1[char] += 1
        for char in word2:
            freq2[char] += 1
        return (set(freq1.values()) == set(freq2.values())
                and sorted(freq1.keys()) == sorted(freq2.keys()))

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        return (set(freq1.values()) == set(freq2.values())
                and sorted(freq1.keys()) == sorted(freq2.keys()))