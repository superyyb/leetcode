class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker = sorted(worker, reverse = True)
        work = sorted(((pro, diff) for pro, diff in zip(profit, difficulty)), reverse = True)
        #等同于work = sorted((zip(profit, difficulty)), reverse = True)
        i, j = 0, 0
        earned = 0
        while i < len(worker) and j < len(work):
            if worker[i] < work[j][1]:
                j += 1
            else:
                i += 1
                earned += work[j][0]
        return earned