class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        In multification, every digit of num1 should times every digit of num2
        So we need a double for loop
        Also how to 错位相加
        '''
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum_val = mul + res[i + j + 1]
                #num1[i] * num2[j] 的个位在 i + j + 1，十位在 i + j
                res[i + j + 1] = sum_val % 10 # 当前位存个位
                res[i + j] += sum_val // 10 # 进位累加到前一位
        start = 0
        while start < len(res) and res[start] == 0:#skip 0
            start += 1
        return "".join(map(str, res[start:]))
        #join只能拼接str，因此需要map(str, res)，把list先转为str


