class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        oper = 0
        ans = k #不需要写float("inf")，因为最多k个W
        for i, x in enumerate(blocks):
            if blocks[i] == "W":
                oper += 1
            if i < k - 1:
                continue
            ans = min(ans, oper)
            if blocks[i - k + 1] == "W":
                oper -= 1
        return ans