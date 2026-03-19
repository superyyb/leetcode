class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0 #初始化结果为0
        pre_values=0
        for i in range(len(s)):
            current_values=roman_values[s[i]]
            if pre_values<current_values:
                result+=current_values-2*pre_values
            else:
                result+=current_values
            pre_values=current_values
        return result
sol=Solution() #创建实例
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))