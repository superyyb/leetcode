#不推荐：time O(log m + n) 应该把for loop再换成binary search（O(log m + log n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        l, r = 0, row - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][col - 1]:
                l = mid + 1
            else:
                for num in matrix[mid]:
                    if target == num:
                        return True
                return False
        return False#为什么要最后再写一个return False
    #如果整个 while 循环结束了，说明目标不可能存在于任何一行，
    #此时你需要一个兜底的 return False。

#推荐；双重binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        l, r = 0, row - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][col - 1]:
                l = mid + 1
            else:
                line = matrix[mid]
                left, right = 0, col - 1
                while left <= right:
                    m = (left + right) // 2
                    if line[m] == target:
                        return True
                    elif line[m] < target:
                        left = m + 1
                    else:
                        right = m - 1
                return False
        return False