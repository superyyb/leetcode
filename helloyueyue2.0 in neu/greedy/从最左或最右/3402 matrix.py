class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        i = 0
        moves = 0
        m = len(grid)  # number of rows
        n = len(grid[0])  # number of columns
        for col in range(n):
            standard = grid[0][col]
            for row in range(1, m):
                if grid[row][col] <= standard:
                    moves += standard - grid[row][col] + 1
                    standard += 1
                else:
                    standard = grid[row][col]
        return moves