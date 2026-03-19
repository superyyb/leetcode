
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        ans = float("inf")
        for i, card in enumerate(cards):
            if card in seen:
                ans = min(ans, i - seen[card] + 1)
            seen[card] = i
        return ans if ans != float("inf") else -1

#sliding window
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        left = 0
        ans = float('inf')
        for right, card in enumerate(cards):
            seen[card] = seen.get(card, 0) + 1
            while seen[card] > 1:
                ans = min(ans, right - left + 1) #更新答案
                seen[cards[left]] -= 1 #缩
                left += 1
        return ans if ans != float('inf') else -1