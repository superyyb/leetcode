# time:O(k*log(k))k为子数组长度 space: O(m)
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        res = [True] * m
        # Round 0: nums[l[0]:nums[r[0]+1]]->nums[0:3]
        # Round 1: nums[l[1]:nums[r[1]+1]]->nums[0:4]
        for i in range(m):
            nums_slice = sorted(nums[l[i]: r[i] + 1])
            target = nums_slice[1] - nums_slice[0]  # 移到for loop外面算，提高效率
            for j in range(2, len(nums_slice)):
                if nums_slice[j] - nums_slice[j - 1] != target:
                    res[i] = False
        return res
