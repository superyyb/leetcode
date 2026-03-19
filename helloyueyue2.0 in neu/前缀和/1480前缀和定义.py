class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        RunningSum = [0] * len(nums)
        RunningSum[0] = nums[0]
        for i in range(1, len(nums)):
            RunningSum[i] = RunningSum[i - 1] + nums[i]
        return RunningSum

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        return nums