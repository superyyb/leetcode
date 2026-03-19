class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        #[1,1,2,2,3,7]
        move = 0
        nums.sort()
        standard = nums[0]
        for num in nums[1:]:
            if num >= standard + 1:
                standard = num
            else:
                move += standard - num + 1
                standard += 1
        return move