class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        #所以low score肯定能取到0，问题在于high score是多少
        n = len(nums)
        if n <= 2:
            return 0
        nums.sort()
        # 三种去掉两个元素的方案，算出剩余区间长度
        return min(
            nums[n-3] - nums[0],#去掉最右边两个
            nums[n-2] - nums[1],#去掉左右各一个
            nums[n-1] - nums[2],#去掉最左边两个
        )