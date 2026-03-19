# 会超时
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n % 4 == 0:
            n //= 4
        return True if n == 1 else False

# 位运算
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n % 3 == 1)