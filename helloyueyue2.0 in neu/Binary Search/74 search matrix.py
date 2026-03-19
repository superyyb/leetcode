#2d->1d 只要一次二分 time:O(log(m * n))  space:O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            elif x < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

#两次二分 time:O(log m + log n)  space:O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Binary search
        1.Target in matrix: True
        2.Target not in matrix: False
        '''
        m = len(matrix)  # 3
        n = len(matrix[0])  # 4
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                i, j = 0, n - 1
                while i <= j:
                    mid2 = (i + j) // 2
                    if target == matrix[mid][mid2]:
                        return True
                    elif target > matrix[mid][mid2]:
                        i = mid2 + 1
                    else:
                        j = mid2 - 1
                return False  # ⚠️只能写在这 而不是在函数结束后
        return False


'''
第一个 return False
    已经确定 target 只能在某一行里，但这一行里没找到
第二个 return False 
    没有任何一行满足：matrix[mid][0] <= target <= matrix[mid][-1]
'''