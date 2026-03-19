from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        in_deg = [0] * numCourses
        res = []
        for a, b in prerequisites: #b -> a
            g[b].append(a)
            in_deg[a] += 1
        q = deque(i for i, d in enumerate(in_deg) if d == 0)
        while q:
            x = q.popleft()
            res.append(x)
            for y in g[x]:
                in_deg[y] -= 1 #因为把x从图中移除就是要邻居都减去一个前置课程
                if in_deg[y] == 0:
                    q.append(y)
        return res if len(res) == numCourses else []
