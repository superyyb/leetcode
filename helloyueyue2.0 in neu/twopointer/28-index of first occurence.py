class Solution:#slice
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


class Solution:#compare every char
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        for i in range(n - m + 1):# 枚举起点
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i
        return -1
