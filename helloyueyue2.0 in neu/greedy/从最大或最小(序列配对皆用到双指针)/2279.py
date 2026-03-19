class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        diff = [0] * n
        for i in range(n):
            diff[i] = capacity[i] - rocks[i]
        diff.sort()
        for i, d in enumerate(diff):
            additionalRocks -= d
            if additionalRocks < 0:
                return i
            elif i == n - 1:
                return i + 1


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        diff = [0] * n
        for i in range(n):
            diff[i] = capacity[i] - rocks[i]
        diff.sort()
        count = 0
        for i in range(n):
            if diff[i] == 0:
                count += 1
            elif diff[i] <= additionalRocks:
                additionalRocks -= diff[i]
                count += 1
        return count