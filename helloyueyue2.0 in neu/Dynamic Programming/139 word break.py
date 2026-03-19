class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dp[i]:
        True if s[:i] can be segmented, otherwise False
        base case: dp[0] = True
        '''
        wordDict_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # 一共有n+1个索引
        dp[0] = True  # dp[0] = 空字符串 s[0:0]  ← base case
        for i in range(n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict_set:
                    dp[i] = True
                    break  # 只是跳出j循环
        return dp[n]
