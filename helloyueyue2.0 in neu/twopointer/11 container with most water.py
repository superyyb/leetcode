class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            h = min(heights[i], heights[j])
            w = j - i
            max_area = max(max_area, h * w)
            if heights[i] <= heights[j]:#比照左右两边总是取更大的height
                i += 1
            else:
                j -= 1
        return max_area