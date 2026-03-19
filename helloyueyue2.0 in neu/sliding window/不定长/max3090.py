class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """
        寻找max length of subarray
        向右扩：记录每个字符出现次数
        左缩：一旦出现次数>2，left右移，减去s[left]出现次数
        """
        left = 0
        n = len(s)
        seen = {}
        max_ans = ans = 0
        for right, x in enumerate(s):
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1
            while seen[x] > 2: #先while loop缩到符合的长度 再更新答案
                seen[s[left]] -= 1
                left += 1
            ans = right - left + 1
            max_ans = max(max_ans, ans)
        return max_ans