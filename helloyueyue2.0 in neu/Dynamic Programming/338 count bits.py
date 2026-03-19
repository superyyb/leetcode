class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Traverse through list:
            for each i: transfer to binary and count 1s
        '''
        res = [0] * (n + 1)
        for i in range(n + 1):
            count = 0
            for char in bin(i):
                if char == '1':
                    count += 1
            res[i] = count
        return res

class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Traverse through list:
            for each i: transfer to binary and count 1s
            i >> 1 / i // 2：去掉最后一位
            i & 1：最后一位是 0 还是 1
        '''
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1]+ (i & 1)
        return dp