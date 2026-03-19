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

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
    #在一个 k × k 的方阵中，要将其行顺序上下翻转，总共需要交换 k // 2 对上下对称的行。
        for i in range(k // 2):
            top = x + i
            bottom = x + k - 1 - i
            grid[top][y : y + k], grid[bottom][y : y + k] = grid[bottom][y : y + k], grid[top][y : y + k]
        return grid