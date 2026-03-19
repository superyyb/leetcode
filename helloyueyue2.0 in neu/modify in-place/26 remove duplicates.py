class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #双指针，i遍历列表，j把不重复元素挪到前面
        i, j = 0, 0
        visited=set()
        while i < len(nums):
            if nums[i] not in visited:
                nums[j] = nums[i]
                j += 1
                visited.add(nums[i])
            i += 1
        return j

"""
总结： 
lc26，27，80 只要保留想要的元素就可以，其他元素不重要，跳过或者覆盖都可
lc283，905 需要整个列表都保留，只改变顺序或位置
"""