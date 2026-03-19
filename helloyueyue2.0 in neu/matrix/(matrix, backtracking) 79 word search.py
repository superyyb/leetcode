class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #DFS
        m = len(board)
        n = len(board[0])
        def dfs(x, y, k):
            if not (0 <= x < m and 0 <= y < n) or word[k] != board[x][y]:
                return False
            if k == len(word) - 1:
                return True
            #backtracking
            temp = board[x][y]
            board[x][y] = "#"
            res = (dfs(x + 1, y, k + 1) or dfs(x - 1, y, k + 1) or
                dfs(x, y - 1, k + 1) or dfs(x, y + 1, k + 1))
            board[x][y] = temp#回溯（还原 board[x][y]），让其他路径还能使用这个格子。
            return res
        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False


from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #multi_BFS 比较复杂 必须每条路径自带 visited，否则不同起点/不同路径会互相“占格子”
        if not board or not board[0]:
            return False
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    q.append((x, y, 0, {(x, y)}))
        while q:
            x, y, k, visited = q.popleft()
            if k == len(word) - 1:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if board[nx][ny] == word[k + 1]:
                        q.append((nx, ny, k + 1, visited | {(nx, ny)}))
        return False