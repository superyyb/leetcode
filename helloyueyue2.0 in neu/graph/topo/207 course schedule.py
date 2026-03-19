from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        in_deg = [0] * numCourses  # in_deg
        res = []
        g = [[] for _ in range(numCourses)]  # adjlist
        for a, b in prerequisites:
            g[b].append(a)  # b -> a 先上b才能上a，从b出发可以走到a
            in_deg[a] += 1
        for i, d in enumerate(in_deg):
            if d == 0:
                q.append(i)
        # 等价于q = deque([i for i, d in enumerate(in_deg) if d == 0])
        while q:
            x = q.popleft()
            res.append(x)
            for y in g[x]:  # 遍历所有依赖 x 的后续课程 y   x->y
                in_deg[y] -= 1
                if in_deg[y] == 0:
                    q.append(y)
        if len(res) != numCourses:
            return False
        return True

