class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        a ^ a = 0（相同的数异或为0）
        a ^ 0 = a
        成对的数全都抵消为0，最后剩下单独的数
        '''
        res = 0
        for num in nums:
            res ^= num
        return res

    '''
        [4,1,2,1,2]
        0 ^ 4 = 4
        4 ^ 1 = 5
        5 ^ 2 = 7
        7 ^ 1 = 6
        6 ^ 2 = 4  ← 只剩下4

        [1,2,1,2]
        0 ^ 1 = 1
        1 ^ 2 = 3
        3 ^ 1 = 2
        2 ^ 2 = 0
    '''

