#Feb 22复盘 BFS起点设反了，不知道怎么更新距离，先更新距离再入队
#⚠️这道题不用visited 可能会“访问检查”多次，但不会“重复入队”，因为设置了if mat[nr][nc] > mat[r][c] + 1:
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        multi-BFS
        1.Start from 0 and find their 1 neighbors
        2.Every BFS round we store a current distance
        3.If we find a 1, check and update the minimum distance
          -Set the distance of every 1 as float('inf')
          -Find a 1, compare its distance(mat[nr][nc]) with current distance + 1
          -Update the minimum distance
        '''
        m = len(mat)
        n = len(mat[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n:
                    if mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr, nc))
                    #只有当我发现更短路径，才更新并入队
        return mat





from collections import deque
class Solution:
# time: O(m*n) = O(N) space: O(m*n) = O(N)   N为元素总数
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        if not mat or not mat[0]:
            return []
        m = len(mat)
        n = len(mat[0])
        dist = [[float('inf')] * n for _ in range(m)]#其实没必要 直接在matrix上记录距离
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):#把所有的0放入q
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    dist[i][j] = 0
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1#舍弃原本 dist[nr][nc]，更新为dist[r][c] + 1
                        q.append((nr, nc))#⚠️只有当一个节点的最短距离被更新时，才值得进一步扩展它。
        return dist

'''
第一轮:
dist[r][c]都是我们预先存在q里的0, dist[nr][nc] 是我们预设的float("inf")
第一轮扩散时，所有与 0 相邻的 1 的距离都会被更新为 1，并加入队列。

之后的扩散（第二轮、第三轮…）:
队列里的点就不再是 0，而是那些刚刚更新为 1 的格子(neighbors)。
某些 1 可能已经被更新过，
只有当新路径更短（> 成立）时才会再次更新。
所以才需要比较 if dist[nr][nc] > dist[r][c] + 1:
'''

