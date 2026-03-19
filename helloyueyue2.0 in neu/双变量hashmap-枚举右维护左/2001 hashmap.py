class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        seen = {}
        count = 0
        for rec in rectangles:
            ratio = rec[0]/rec[1]
            count += seen.get(ratio, 0)
            seen[ratio] = seen.get(ratio, 0) + 1
        return count