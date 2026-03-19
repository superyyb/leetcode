class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1
        min_val = float("inf")
        for i, num in enumerate(nums):
            if num <= min_val:#注意像[5,5,5]明明应该返回-1却返回0
                min_val = num
            elif num - min_val > diff:
                    diff = num - min_val
        return diff