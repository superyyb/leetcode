class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        求从队首/尾取出的k个元素max_sum，
        转换思路即求队中n-k个元素的min_sum,定长n-k滑动窗口
        """
        n = len(cardPoints)
        total = 0
        for i in range(n):
            total += cardPoints[i]
        ans = total
        curr_sum = 0
        L = n - k  # n = k 的特例
        if L == 0:
            return total
        for i, x in enumerate(cardPoints):
            curr_sum += x
            if i < L - 1:  # 如果忽略了n=k， 则直接进入i < –1
                continue
            ans = min(ans, curr_sum)
            curr_sum -= cardPoints[i - L + 1]
        return total - ans
