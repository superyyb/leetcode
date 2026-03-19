class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        Goal: Generate an n*n matrix and fill in number
        Everytime shrink the boundary if we finish traversing one line
        top, bottom, left, right
        '''
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        target = n * n
        while num <= target:
            # 1. From left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            # 2. From top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            # 3. From right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            # 4. From bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix


