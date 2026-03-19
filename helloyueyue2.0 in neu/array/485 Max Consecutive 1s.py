class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        1.Traverse through the list
        2.If 1: add to curr_total.   If 0: update max_total and reset curr_total to 0
        '''
        max_total, curr_total = 0, 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 1:
                curr_total += 1
                max_total = max(max_total, curr_total)
            else:
                curr_total = 0
        return max_total