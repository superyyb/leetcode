#time:O(k) space:O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    '''
    如果最后一位是 1 → n & 1 = 1
    如果最后一位是 0 → n & 1 = 0
    '''

#time:O(k) space:O(k) (bin()生成了string)
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_n = bin(n)
        count = 0
        for digit in binary_n:
            if digit == '1':
                count += 1
        return count