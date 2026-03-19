class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):# 逐个求 dp[3], dp[4], ... dp[n]
            for j in range(1, i // 2 + 1):#对每个i 取i的一半作为j
                dp[i] = max(j * (i - j), j * dp[i - j], dp[i])
        return dp[n]

    """
        对于每个 i ∈ [3, n]，尝试将 i 拆分成两个数 j 和 i - j，有两种选择：
    	1.不再继续拆 i - j：乘积为 j * (i - j)
    	2.继续拆 i - j：乘积为 j * dp[i - j]
        然后取这两者中的最大值，作为当前 dp[i] 的候选项。
    """


    """
    把 i 切成 j 和 i-j 两段时，有四种可能：
    两边都不再分：j * (i-j)
    只分右边：j * dp[i-j]
    只分左边：dp[j] * (i-j)。不用显式写出来，因为当外层循环的 i 增加时，
    之前计算过的 dp[j] 已经记录了“左边继续拆”的最优结果。
    两边都分
    """

