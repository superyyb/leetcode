class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Depth-first search
        1.Traverse through the string word. Start with the first letter
        2.Mark whether the cell is visited
        3.Pruning: If the letter is not in board: break and return False
        '''
        if not board or not board[0]:
            return False
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, k) -> bool:
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = '#'  # Mark as visited
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                if dfs(nr, nc, k + 1):  # ⚠️dfs需要返回值
                    board[i][j] = temp
                    return True
            board[i][j] = temp  # ⚠️ 重点：所有方向都走不通，也要回溯！
            return False  # 显式返回 False

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:  # 只有当首字母匹配时才开始dfs
                    if dfs(i, j, 0):
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