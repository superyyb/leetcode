class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        #left
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        #overlap
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        #right
        while i < n:
            res.append(intervals[i])
            i += 1
        return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        inserted = False
        for start, end in intervals:
            if end < new_start:  #left
                res.append([start, end])
            elif start > new_end: #放入right之前把新interval放进去
                if not inserted:
                    res.append([new_start, new_end])
                    inserted = True
                res.append([start, end])
            else:#3. 有重叠，更新边界，不要 append！因为有可能不止一个区间重叠
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        if not inserted:# for 循环结束后，可能一直在合并，还没插进去
            res.append([new_start, new_end])
        return res