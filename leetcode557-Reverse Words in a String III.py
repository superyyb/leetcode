
"""
split用法
s = "Let's take LeetCode contest"
print(s.split()) 默认忽略连续空格
# ['Let's', 'take', 'LeetCode', 'contest']

s2 = "apple,banana,orange"
print(s2.split(","))
# ['apple', 'banana', 'orange']

join用法
words = ['Let\'s', 'take', 'LeetCode', 'contest']
print(" ".join(words))
# Let's take LeetCode contest

words2 = ['apple', 'banana', 'orange']
print(",".join(words2))
# apple,banana,orange

"""
#yy思路：用split()将字符串转换为列表，遍历列表元素，将每个元素reverse，再join
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        reversed_list=[]
        for items in s_list:
            reversed_item=items[::-1]
            reversed_list.append(reversed_item)
        return " ".join(reversed_list)


#解法二：直接在字符串中添加：不过也要将原str拆成list
#先单词内部反转，再整个句子反转
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        spl = s.split(" ")
        for i in spl:
            res += i[::-1] + " "
        return res[:-1]
 #要删掉最后添加的""（在字符串末尾），所以只能到倒数第二位
