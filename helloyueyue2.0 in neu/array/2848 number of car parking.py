#time: O(U) space:O(k) k:number of 不重复的points
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        occupied = set()
        for num_pair in nums:
            i, j = num_pair[0], num_pair[1]
            while i <= j:
                occupied.add(i)
                i += 1
        return len(occupied)

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        #line sweep: 1 <= nums.length <= 100 适合坐标上界已知
        line = [0] * 102
        points = 0
        for s, e in nums:
            line[s] += 1
            line[e + 1] -= 1
        cur = 0
        for i in range(1, 101):
            cur += line[i]
            if cur > 0:
                points += 1
        return points
    """
    [[1,3],[5,8]]
    line:[0,1,0,0,-1,1,0,0,0,-1]
    cur:1,1,1,0,1,1,1,1,0   points = 7
    """
