#yy思路：
# 遍历str中的元素，if为vowel，
# 把所有vowel拎出来创建一个list，反转list，再把list插入原先的str
import re
class Solution:
    def reverseVowels(self, s: str) -> str:
        pattern=r'[aeiouAEIOU]' #使用正则表达式匹配vowel字母
        vowels=re.findall(pattern,s)#提取s中所有vowel字母
        vowels.reverse()#反转vowel字母
        # 替换元音字母的替换函数
        def replace_vowel(match):
        # 从反转后的元音字母列表中依次取出字母
            return vowels.pop(0)
        #pop(0):移除 vowels 列表中的第一个（即索引为 0 的元素）。
        # 返回被移除的元素,列表 vowels 中剩余的元素向前移动一个位置。
        result = re.sub(pattern, replace_vowel, s)# 使用 re.sub 函数替换元音字母
        return result
sol=Solution()
s1="hello"
s2="leetcode"
print(sol.reverseVowels(s1))
print(sol.reverseVowels(s2))

#双指针法
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        n=len(s)
        i,j=0,n-1
        vowels=set('AEIOUaeiou')
        while i<j:
            #以下两个while用来跳过不是vowel的字母
            while i<j and s[i] not in vowels:
                i+=1
            while i<j and s[j] not in vowels:
                j-=1
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        s=''.join(s)
        return s
# #为什么要把s先转为list再转回string：
# 字符串是不可变对象，一旦创建，它的内容就不能被修改。
# 如果想要修改字符串中的某些字符（比如交换位置），就必须先将字符串转换为可变对象，
# 例如列表，进行操作后再转换回字符串。