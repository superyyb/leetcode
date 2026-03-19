from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        ans = 0
        n = len(s)
        left = 0
        cnt = defaultdict(int)
        for right, char in enumerate(s):
            cnt[char] += 1
            max_freq = max(max_freq, cnt[char])
            while right - left + 1 - max_freq > k:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
'''
dict：访问不存在的键会 KeyError。
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
defaultdict(int)：访问不存在的键会自动创建该键，并把值设为 int() 的结果（即 0）。
    freq = defaultdict(int)
    for ch in s:
        freq[ch] += 1  # ✅ 自动把 cnt['A'] 视作 0，再加 1
Counter()
    count = Counter(s) 返回一个字典
    s = 'abracadabra'  Counter(s) = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
    所以可以用Counter(s).items(), Counter(s).values()和字典一样的用法
'''