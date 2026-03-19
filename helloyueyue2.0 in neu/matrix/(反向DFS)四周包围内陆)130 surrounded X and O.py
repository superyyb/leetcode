class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
            Do not return anything, modify board in-place instead.
    1.先把边界上的"O"转为别的字母比如E
    2.把剩下的"O"转为X
    3.把E转回"O"
        """
        # time, space: O(m*n)
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