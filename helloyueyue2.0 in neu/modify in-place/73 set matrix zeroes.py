#time: O(m * n) space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #❌直接把首行首列变成0，再根据首行首列调整
        #matrix[0][0]既属于第一行，也属于第一列。
        #如果用 matrix[0][0] 来标记“第一行是否需要置零”；
        #用什么来标记“第一列是否需要置零”呢？
        m = len(matrix)
        n = len(matrix[0])
        #单独记录首行首列是否有0 -> 跳过首行首列，从 (1, 1) 开始遍历中间部分来做标记
        row0_has_zero = False
        col0_has_zero = False
        for j in range(n):#check if first row contains zero
            if matrix[0][j] == 0:
                row0_has_zero = True
                break
        for i in range(m):#check if first column contains zero
            if matrix[i][0] == 0:
                col0_has_zero = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0] * n
                #for j in range(1, n):
                    #matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if row0_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        if col0_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        return matrix


#time: O(m * n) space: (O(m+n))
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Mark-traversal problem
        #use hashmap/set
        zero_rows = set()
        zero_cols = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for row in zero_rows:
            matrix[row] = [0] * n
        for col in zero_cols:
            for i in range(m):
                matrix[i][col] = 0
        return matrix

