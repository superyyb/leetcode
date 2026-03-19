#Time: O(nlogn) Space: O(n) inbuilt sort
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # two pointers - l for tracking face up & r for tracking face down
        tokens.sort()
        l, r = 0, len(tokens) - 1
        curr_score = max_score = 0
        while l <= r: #Three cases
            if tokens[l] <= power: #face up:choose the smallest power to earn scores
                power -= tokens[l]
                curr_score += 1
                max_score = max(max_score, curr_score)
                l += 1
            elif curr_score >= 1:#face down:choose the largest power to earn powers
                power += tokens[r]
                curr_score -= 1
                r -= 1
            else: #impossiable to play
                break
        return max_score