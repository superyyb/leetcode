class Solution:
    def reverse(self, x: int) -> int:
        #1.先处理符号
        sign = -1 if x < 0 else 1
        #2.反转
        x = str(abs(x))[::-1]
        res = int(x) * sign
        #3.检查是否溢出
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
'''
解法劣势：
1.经历多次int,str转变，产生多余内存开销
2.先反转再检查溢出，有可能反转之后就已经产生了超出 64 位范围的巨大中间值
'''

#time: O(m) m = length of x   space: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        '''
        %: 余数。对一个整数进行 % 10得到它的个位数。
        //: 整数商。对一个整数进行 // 10，相当于把它的个位数“砍掉”。
        '''
        # 1. 处理符号
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x != 0:
            # 2. 剥下最后一位
            digit = x % 10
            # 3. 准备去掉 x 的最后一位
            x //= 10
            # 4. 拼接到结果中
            res = res * 10 + digit
        # 5. 加回符号
        res *= sign
        # 6. 32位溢出检查
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
