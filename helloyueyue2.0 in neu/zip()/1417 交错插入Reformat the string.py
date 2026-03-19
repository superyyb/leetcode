#time$space: O(n)
class Solution:
    def reformat(self, s: str) -> str:
        digit = []
        alpha = []
        list_s = list(s)
        for i in range(len(s)):
            if list_s[i].isdigit():
                digit.append(list_s[i])
            else:
                alpha.append(list_s[i])
        if abs(len(digit) - len(alpha)) > 1:
            return ""
        else:
            res = []
            if len(alpha) > len(digit):
                for num, letter in zip(digit, alpha):#⚠️zip用法
                    res.append(letter)
                    res.append(num)
                res += alpha[-1]
            elif len(digit) > len(alpha):
                for num, letter in zip(digit, alpha):
                    res.append(num)
                    res.append(letter)
                res += digit[-1]
            else:
                for num, letter in zip(digit, alpha):
                    res.append(num)
                    res.append(letter)
            return ''.join(res)