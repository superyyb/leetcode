class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        #有一个subarray的首值是固定的 即nums[0]
        subnums = sorted(nums[1 : ])
        return nums[0] +subnums[0] +subnums[1]