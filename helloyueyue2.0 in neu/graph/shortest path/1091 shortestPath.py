#普通bfs 不是0/1bfs，不需要比较更新dist
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1
        dist = [[float("inf")] * n for _ in range(m)]
        q = deque([(0, 0)])
        dist[0][0] = 1
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        while q:
            r, c = q.popleft()
            if (r, c) == (m - 1, n - 1):#⚠️记得及时返回
                return dist[r][c]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 1:
                    if dist[nr][nc] == float("inf"):#“如果通过当前格子 (r,c) 再走一步到 (nr,nc)，能得到更短的路径，那我就更新它。”
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))#⚠️只有当一个节点的最短距离被更新时，才值得进一步扩展它。
        return -1

    '''
在 Dijkstra / 0-1 BFS 里，我们要比较：if nd < dist[nx][ny]:
因为那里边的「代价」可能不一样（有的边是 0、有的是 7），
所以一个节点可能后来出现更短的路径。

但在普通 BFS 里，每条边权 = 1：
	•⚠️只要你第一次访问到这个节点，它的距离就已经是最小值；
	•后面再访问时，必然步数更大，不可能更短；
	所以我们只需要判断：if dist[nx][ny] == inf:  # 还没访问过

特性	         普通 BFS	        0-1 BFS 	    Dijkstra
边权	         全为 1	            只有 0 / 1	    任意非负数
队列结构	    deque（普通队列） 	deque（双端）	heapq（堆）
距离更新条件	== inf（没访问过）    <（发现更短） 	<（发现更短）
    '''