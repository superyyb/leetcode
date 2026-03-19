from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        '''
        1.Find the path to the end which contains the least 1
        2.Find the shortest path(consider 0/1 is the step)
        '''
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = [[float("inf")] * n for _ in range(m)]#⚠️用 dist 2d数组记录每个格子从起点开始的最短dist
        q = deque([(0, 0)])
        dist[0][0] = grid[0][0]#⚠️
        while q:
            x, y = q.popleft()
            d = dist[x][y]#⚠️
            if d >= health:#pruning
                continue
            if x == m - 1 and y == n - 1:#pruning#⚠️直接返回答案
                return d < health
            for dc, dr in directions:
                dx, dy = dc + x, dr + y
                if 0 <= dx < m and 0 <= dy < n:
                    nd = d + grid[dx][dy]
                    if nd < dist[dx][dy] and nd < health:
                        dist[dx][dy] = nd
                        if grid[dx][dy] == 0:
                            q.appendleft((dx, dy))
                        else:
                            q.append((dx, dy))
        return dist[m - 1][n - 1] < health
    '''
    if d >= health:#pruning
        continue
    d 是当前走到 (x, y) 的代价（经过的危险格数）
    如果 d >= health，说明：
	•你已经踩了太多危险格（生命值 ≤ 0），
	•即使继续走，也不会成功，所以没有必要再从这个节点扩展周围的格子。
于是 continue 让程序直接跳过当前 while 循环的剩余部分，继续从队列中取下一个点。
    '''
    '''
从 (x, y) 走到 (nx, ny) 要花费代价 grid[nx][ny],所以新的路径代价是：
        nd = dist[x][y] + grid[nx][ny]
        '''