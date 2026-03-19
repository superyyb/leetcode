"""
前缀和变式：
需要把是否首尾vowel的布尔问题转变为数值问题
words = ["aba","bcb","ece","aa","e"]
A = [1 if w[0] in vowels and w[-1] in vowels else 0 for w in words]
结果:
"aba" → 'a'/'a' 都是元音 → 1
"bcb" → 'b'/'b' 不是元音 → 0
"ece" → 'e'/'e' 是元音 → 1
"aa"  → 'a'/'a' 是元音 → 1
"e"   → 'e'/'e' 是元音 → 1
所以 A = [1, 0, 1, 1, 1]
基于 A 构造前缀和 P：
P = [0, 1, 1, 2, 3, 4]
针对每个查询 [l, r]，答案就是P[r+1] - P[l]
"""
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        Prefix = [0] * (n + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(n):
            Prefix[i + 1] = Prefix[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                Prefix[i + 1] += 1
        res = []
        for q in queries:
            res.append(Prefix[q[1] + 1] - Prefix[q[0]])
        return res