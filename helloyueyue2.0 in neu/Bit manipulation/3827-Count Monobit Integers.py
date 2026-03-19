#暴力法 time O(nlogn)
class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0
        for i in range(n + 1):
            if len(set(list(format(i, 'b')))) == 1:
                count += 1
        return count

#最优解 time O(logn)
class Solution:
    def countMonobit(self, n: int) -> int:
        '''
对应的十进制数其实是有规律的。全 1 的二进制数等于 2**k−1：
        '''
        if n == 0:
            return 1
        count = 1  # 初始计入数字 0
        k = 1
        while (2 ** k - 1) <= n:
            count += 1
            k += 1
        return count