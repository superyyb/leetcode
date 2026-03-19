class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        #greedy策略：从最小的开始加，2，4，6...
        if finalSum % 2 != 0:
            return []
        res = []
        i = 1
        while finalSum >= 2*i:
            finalSum -= 2*i
            res.append(2*i)
            i += 1
        if finalSum > 0:
            res[-1] += finalSum
        return res