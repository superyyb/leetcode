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

class Solution: #left/right-bound
    def sortColors(self, nums: List[int]) -> None:
        left, i, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1 #left_bound向右移一位
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1