#⚠️ nodes labeled from 1 to n 建图记得取range(n + 1)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [0] * (n + 1)
        cycle = set()
        cycleStart = -1
        def dfs(i, parent):#dfs检测是否有环
            nonlocal cycleStart
            visited[i] = 1
            for j in g[i]:
                if j == parent:#j is visited and j is parent
                    continue
                if visited[j]: #j is visited and not parent
                    cycleStart = j
                    cycle.add(i)
                    return True
                if dfs(j, i):  #j is not visited
                        if cycleStart != -1:
                            cycle.add(i) #backtracking
                        if cycleStart == i:# 回到环入口，收集结束
                            cycleStart = -1
                        return True
            return False
        dfs(1, -1)  # 题目保证图是连通的，从 1 出发即可
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []
    """
    找多余的边 其实就是找到图中的环，做标记 
    再从后往前遍历找到第一个在环中的边

    记录三种状态  0=未访问, 1=正在访问, 2=已访问
    """