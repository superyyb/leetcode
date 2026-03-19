#2026 2.20复盘 忘记fresh = 0时return 0
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Input: grid  Output: mini minutes
        algo:BFS
        1.Traverse through the grid to count the total number of oranges and mark the number and coordinate of rotten oranges
        2.Start BFS with rotten oranges, find and mark its neighbors as rotten
        3.Count the round of BFS as the minutes
        4.Every BFS round: total number - number of affected oranges
        4.Return the minutes if all oranges are rotten else -1
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)  # row
        n = len(grid[0])  # col
        q = deque()
        total = 0
        rotten = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    rotten += 1
                elif grid[i][j] == 0:
                    continue
                total += 1
        if total - rotten == 0:
            return 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            rotten += 1
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            time += 1
        return time - 1 if rotten == total else -1


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi BFS
        """
        忘记的点：
        1.统计fresh数量,没有考虑有fresh永远传不到的情况
        2.q的每一层有fresh被感染 才需要time+= 1 不能盲目加
        3.没有考虑初始就没有需要腐烂的情况fresh == 0,答案应该是 0(答案在最后一行)
        """
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        q = deque()
        time, fresh = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:#没有fresh，直接return0
            return 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q and fresh > 0:
            for _ in range(len(q)):#⚠️一定要分层
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))# 有新元素入队 => 本层确实发生了感染
            if q: #这一层的所有感染完成后，才算过了一分钟，所以缩进在这
                time += 1
        return time if fresh == 0 else -1
    """
易错点：容易把“分钟”按每个节点加1；但题里时间应该按一层（同一分钟内同时腐烂的那批）来加。
    应该用分层 BFS（按当前队列大小循环），每处理完一层才 time += 1

    把所有rotted orange一次性入队作为多个起点，按层扩散；每一层=1 min。复杂度 O(mn)，空间 O(mn)（最坏队列装下整层）。
    
    """
#复盘
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi BFS
        #再次做忘记：
        #统计fresh数量
        #一定有fresh被感染 time才能加1
        if not grid or not grid[0]:
            return 0
        q = deque()
        m = len(grid)
        n = len(grid[0])
        time, fresh = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:#⚠️
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))# ⚠️有新元素入队 => 本层确实发生了感染
            if q:
                time += 1
        return time if fresh == 0 else -1