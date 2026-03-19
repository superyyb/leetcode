#最优解
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_searching_left):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid#⚠️必须先更新idx，因为最后一次必定是不满足条件退出循环，所以要留下最后一次之前的结果
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx

        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        return [left, right]
    '''
    每次遇到 target：
    idx 都被更新为 当前合法位置
    while 结束时：
    左右边界已经被压到极限
    idx 保存的是最后一次遇到的边界位置
    '''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
       Binary search
       1.Target found: return [start, end]
       2.Target not found: return [-1, -1]
        '''
        res = [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2 #[5,7,7,8,8,10]
            if nums[mid] < target:#to get leftmost target
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
        if left < len(nums) and nums[left] == target:
            res[0] = left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:#to get rightmost target
                right = mid - 1
            elif nums[mid] <= target:
                left = mid + 1
        if right >= 0 and nums[right] == target:
            res[1] = right
        return res

'''
为什么必须写 if left < len(nums) ：
左边界查找结束后：left == 第一个 >= target 的位置
情况	                left 的值
target 存在	    指向第一个 target
target 不存在	可能 == len(nums) ❗
'''

