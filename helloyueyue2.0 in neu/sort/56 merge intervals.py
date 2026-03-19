"""
1.Sort first
2.Compare the start of current interval with the end of previous interval
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:(x[0], x[1]))
        merged = [intervals[0]]
        for interval in intervals[1:]:
            prev = merged[-1]
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(interval)
        return merged