class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        1.Must sort first  [[2,3],[1,5]]
        2.Compare the right bound of the previous interval with the left bound of current one
        3.If right prev >= left curr -> update prev[1]
        4.Add to res
        '''
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = res[-1]
            curr = intervals[i]
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(curr)
        return res


#Jan6❌解
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Why merge?
        1.Compare the right bound of the previous interval with the left bound of current one
        2.If right prev >= left curr -> merge
        '''
        intervals.sort()
        res = []#❌没有处理第一个interval
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            if prev[1] >= curr[0]:
                res.append([prev[0], curr[1]])#不是一次性的，是要一直更新prev[1]
            else:
                res.append(intervals[i])
        return res

#Feb21解
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals = [[1,3],[2,6],[3,4],[8,10],[15,18]]
        #[[1,4],[4,7]]
        '''
        1.Sort the intervals
        2.Compare the x1 of last interval in result with x0 of the first underdecided interval
        3.If there is an intersection:
            Merge
          else:
            Append to result
        '''
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][-1], interval[1])
            else:
                res.append(interval)
        return res


