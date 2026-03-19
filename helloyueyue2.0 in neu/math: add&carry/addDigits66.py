class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        1. Normal case:                     [4,3,2,1] -> [4,3,2,2]
        2. carry 1 to the bigger digits:    [9] -> [10]
                                            [9,9,9] -> [1,0,0,0]
        ❌Transfer list into int
        digits可能非常长，考察的是加法进位
        '''
        n = len(digits)
        for i in range(n - 1, -1, -1):#inverted order
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0   # 当前位是 9，变 0，继续进位
        # 能走到这里，说明全是 9
        return [1] + digits