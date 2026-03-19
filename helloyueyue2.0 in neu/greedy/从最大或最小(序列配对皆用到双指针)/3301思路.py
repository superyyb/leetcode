class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        if len(set(maximumHeight)) == len(maximumHeight):
            return sum(maximumHeight)
        prev = float("inf")
        total = 0
        maximumHeight.sort(reverse=True)
        for h in maximumHeight:
            assigned = min(prev - 1, h)#必须比prev小且不能超过h
            total += assigned
            if assigned <= 0:
                return -1
            prev = assigned
        return total