class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #How to carry in binary
        #Two pointers start in the end of strings
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            if s == 0:
                res.append('0') #0%2
                carry = 0       #0//2
            elif s == 1:
                res.append('1') #1%2
                carry = 0       #1//2
            elif s == 2:
                res.append('0') #2%2
                carry = 1       #2//2
            else:#s==3
                res.append('1') #3%2
                carry = 1       #3//2
        return "".join(reversed(res))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            res.append(str(s % 2))
            carry = s // 2
        #当前位 = 总和减去进位后的剩余
        #进位 = 总和里能凑出几个 2
        return "".join(reversed(res))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        binary % 2 = 看最后一位是 0 还是 1
        binary // 2 = 右移一位（删掉最后一位）
        s % 2   得当前位. 1101 % 2 = 1
        1101 = 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0
             = 2*2^2 + 2*2^1 + 2*0 + 1*2^0
        s // 2  得进位 1101//2 = 110
        '''
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            x = ord(a[i]) - ord('0') if i >= 0 else 0
            y = ord(b[j]) - ord('0') if j >= 0 else 0
            s = x + y + carry
            res.append(str(s % 2))
            carry = s // 2
            i -= 1
            j -= 1

        return ''.join(res[::-1])

    '''
        在这道题中：我们把str转换成int之后：
            x ∈ {0,1}
            y ∈ {0,1}
            carry ∈ {0,1}
            所以s = x + y + carry 只可能是十进制的 {0,1,2,3}
            在任何一步中，s 永远只会是：0, 1, 2, 或 3 
            s     s              当前位     进位     s%2    s//2
            0    00   不需要进位    0         0       0       0
            1    01   不需要进位    1         0       1       0
            2    10   需要进位      0         1       0       1
            3    11   需要进位      1         1       1       1
        '''