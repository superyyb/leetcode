#dp
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
    dp[i][j] = s[:i] 是否是 t[:j] 的子序列
        """
        m = len(s)
        n = len(t)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[m][n]
    """
	若 s[i-1] == t[j-1] → 可以匹配这一个字符：
        dp[i][j] = dp[i-1][j-1]
	否则跳过 t[j-1]：
        dp[i][j] = dp[i][j-1]
    """


#two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1
        return i == len(s)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = list(s)
        for char in t:
            if queue and queue[0] == char:
                queue.pop(0)
                # If all characters in s have been matched, we can break early.
                if not queue:
                    break
        return len(queue) == 0

=