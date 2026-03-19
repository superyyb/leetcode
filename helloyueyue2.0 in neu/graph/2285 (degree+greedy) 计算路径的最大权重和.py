#最优解
"""
(i+1) * d 其实就是：
	•(i+1) = 这个城市分到的价值
	•d = 这个城市的度数
	•乘起来 = 这个城市对总和的贡献
"""
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
    #greedy:degree越小，分到的价值越小
        deg = [0] * n
        for u, v in roads:#count degree
            deg[u] += 1
            deg[v] += 1
        deg.sort() #1,2,2,3,4
        total = 0
        for i, d in enumerate(deg):
            total += (i + 1) * d
        return total

#用字典 累赘
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        g = {}
        for x, y in roads:
            g[x] = g.get(x, 0) + 1
            g[y] = g.get(y, 0) + 1
        sorted_g = dict(sorted(g.items(), key=lambda x: x[1], reverse=True))
        new_g = {}
        rank = len(sorted_g)
        for key, val in sorted_g.items():
            new_g[key] = n
            n -= 1
        total = 0
        for x, y in roads:
            val = new_g[x] + new_g[y]
            total += val
        return total