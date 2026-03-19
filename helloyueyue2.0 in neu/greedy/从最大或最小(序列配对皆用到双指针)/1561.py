class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        total = 0
        piles = sorted(piles, reverse = True)
        for i in range(1, 2 * n // 3, 2):
            total += piles[i]
        return total