class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
    """
    定义：dp[i] 表示有 i 个节点时，能构造的不同 BST 的总数
    公式： dp[i] += dp[以j为头结点左子树节点数量] * dp[以j为头结点右子树节点数量]

    根节点	左子树大小	右子树大小	方案数
     1	      0	        2	 dp[0]*dp[2] = 1*2
     2	      1	        1	 dp[1]*dp[1] = 1*1
     3	      2	        0	 dp[2]*dp[0] = 2*1
    dp[3] = 2 + 1 + 2 = 5
    """