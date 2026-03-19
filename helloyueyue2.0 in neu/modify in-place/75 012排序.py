#三指针一次遍历
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, i, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            #⚠️这里 i 不能 +1

    '''
    看到 0：放到左边界 left
    看到 2：放到右边界 right ⚠️为什么️这里 i 不能 +1
        当 nums[i] == 2 时：
            你把它换到 right
        但 nums[i] 是从未知区换回来的，必须再判断一次
    看到 1：留在中间 i正常遍历
    '''

class Solution:#啰嗦
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [2,0,2,1,1,2] zero=1 one=2 two=3
        zero, one, two = 0, 0, 0
        for n in nums:
            if n == 0:
                zero += 1
            elif n == 1:
                one += 1
            else:
                two += 1
        for i in range(0, zero):
            nums[i] = 0
        for i in range(zero, zero + one):
            nums[i] = 1
        for i in range(zero + one, len(nums)):
            nums[i] = 2

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3  # [0,2,1,1,2,0] count=[2,2,2]
        for num in nums:
            count[num] += 1
            index = 0
            for i in range(3):  # i = 0, 1, 2
                for _ in range(count[i]):
                    nums[index] = i
                    index += 1

