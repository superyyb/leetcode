class Solution:
    def minimumLength(self, s: str) -> int:
        count = len(s)
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            char = s[i]
            while i <= j and s[i] == char:#用while一次性删所有左边重复字符
                i += 1
            while i <= j and s[j] == char:#用while一次性删所有右边重复字符
                j -= 1
        return j - i + 1