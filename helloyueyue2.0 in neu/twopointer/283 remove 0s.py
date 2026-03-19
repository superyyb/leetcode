class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #two-pointer i for traversing through list, j for pointing at zero
        i, j = 0, 0 #swap
        while i < len(nums):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i], nums[j]
                j += 1
            i += 1
'''
1.如果数组开头都是非零数，比如 [1, 2, 3, 0, ...]：
当 i 在处理 1, 2, 3 的时候，j 也是同步跟着走的。
此时 i == j，所谓的交换其实是自己和自己交换。在这个阶段，j 指向的是非零数。

2.一旦 i 遇到了第一个 0，if nums[i] != 0 就不成立了，此时：
i 继续往前走寻找下一个非零数。
j 则会停在那个 0 的位置上。
从这一刻起，j始终指向第一个可用的 0，等待着 i 从后面运送非零数过来填坑。
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two-pointer i for reading zeros, j for overwriting the list
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        for i in range(j,len(nums)):
            nums[i] = 0