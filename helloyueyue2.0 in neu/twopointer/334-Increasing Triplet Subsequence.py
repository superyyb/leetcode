class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        Two-pointer
        first: the smallest number
        second: the second smallest number
        '''
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else: #num > first and num > second, the third num founded
                return True
        return False