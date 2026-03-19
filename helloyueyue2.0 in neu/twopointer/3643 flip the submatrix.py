class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        #双指针
        i = x
        j = x + k - 1
        while i <= j:
            grid[i][y : y + k], grid[j][y : y + k] = grid[j][y : y + k], grid[i][y : y + k]
            i += 1
            j -= 1
            if i == j:
                break
        return grid