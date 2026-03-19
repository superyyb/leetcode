class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Transpose行变成列，列变成行 A[i][j] → A[j][i]
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):#transfer row i to col i
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()