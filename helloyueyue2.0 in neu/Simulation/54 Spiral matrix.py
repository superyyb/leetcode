class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Goal: Generate a list from matrix in spiral order
        Everytime shrink the boundary if we finish traversing one line
        top: The top row which hasn't been traversed
        bottom: The bottom row which hasn't been traversed
        left: The leftmost column which hasn't been traversed
        right: The rightmost column which hasn't been traversed
        '''
        m = len(matrix)
        n = len(matrix[0])
        if not matrix:
            return []
        # 1.Initialize four boundaries
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []
        while True:
            # 2.Traverse from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            # 3.Traverse from top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            # 4.Traverse from right to left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            # 5.Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res




