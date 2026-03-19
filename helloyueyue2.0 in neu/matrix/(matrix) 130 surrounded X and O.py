class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
            Do not return anything, modify board in-place instead.
    1.先把边界上的"O"转为别的字母比如E
    2.把剩下的"O"转为X
    3.把E转回"O"
        """
        if not board or not board[0]:
            return None
        m = len(board)
        n = len(board[0])
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
                return
            board[i][j] = "E"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)#把和边界O连在一起的O全找出来
        for i in range(m):#检查四条边
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"

#BFS解法
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        BFS:
        1.Start from 4 boundaries of board and find cell'o', push them into queue
        2.Find neighbor cells of the cell'0' and repeat step1
        3.Mark the cell above as 'v'
        4.Traverse through board, Mark '0' as 'x', mark 'v' as '0'
        '''
        m = len(board)
        n = len(board[0])
        q = []#这里用deque更快
        # Check all cell'O' in the four boundaries, mark as 'v'and push them into queue
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
                board[i][0] = 'v'
            if board[i][n - 1] == 'O':
                q.append((i, n - 1))
                board[i][n - 1] = 'v'
        for j in range(n):
            if board[0][j] == 'O':
                q.append((0, j))
                board[0][j] = 'v'
            if board[m - 1][j] == 'O':
                q.append((m - 1, j))
                board[m - 1][j] = 'v'
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.pop(0)
            # Find and mark their neighbors
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    q.append((nr, nc))
                    board[nr][nc] = 'v'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'v':#可以在一遍循环里完成，只要用elif，因为格子不会回头判断
                    board[i][j] = 'O'