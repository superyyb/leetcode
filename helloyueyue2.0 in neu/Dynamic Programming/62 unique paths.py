class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[0] * n for _ in range(m)]
        #分别设置第一行和第一列的base case
        for i in range(m):#每行的第一列
            dp[i][0] = 1
        for j in range(n):#每列的第一行
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]