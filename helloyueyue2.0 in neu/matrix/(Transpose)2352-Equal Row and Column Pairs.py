class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    grid_1 = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]

    1.Generate transposition grid
    2.Compare the rows/cols in these two grids and store the count
        '''
        n = len(grid)
        grid_1 = [[0]*n for _ in range(n)]
        for i in range(n):#transposition列变行
            for j in range(n):
                grid_1[j][i] = grid[i][j]
        count = 0
        for row in grid:
            for col in grid_1:
                if row == col:
                    count += 1
        return count
    '''
    #❌解：        
    for row in grid:
        if row in grid_1: 
            count += 1
    #不会计算重复的 比如 [1,1] [1,1] 答案应该是4，我只算出2
    '''

#用.count()函数
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grid_1 = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                grid_1[j][i] = grid[i][j]
        # 统计每个 row 在 grid_1 中出现的次数
        res = 0
        for row in grid:
            res += grid_1.count(row)  # ✓ 统计出现次数
        return res