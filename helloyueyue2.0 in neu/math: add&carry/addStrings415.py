#双指针 从末尾开始遍历
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        s % 10取余 得到当前这一位   13 % 10 = 3
        s // 10 得到下一轮要加的进位 13 // 10 = 1
        '''
        i, j = len(num1) - 1, len(num2) - 1#123 58
        res = []
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            num1_d = int(num1[i]) if i >= 0 else 0
            num2_d = int(num2[j]) if j >= 0 else 0
            num = (num1_d + num2_d + carry) % 10
            carry = (num1_d + num2_d + carry) // 10
            i -= 1
            j -= 1
            res.append(str(num))
        return "".join(res[::-1])

