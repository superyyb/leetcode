class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       #min_speed:1.  max_speed:max(piles)
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid#❕pile/mid如何向上取整
            if time <= h:
                r = mid - 1# 可以吃完
            else:
                l = mid + 1  # 吃不完
        return l
    """
如何确定return l还是return r：
    我们在做的是 最小化问题（找最小的可行速度）。
	•所以要保证最后收敛时，l 指向第一个可行解。
	•而 r 最终会停在 最后一个不可行解。
    """