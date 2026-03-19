'''
题目：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
'''
#yy思路：将正整数的每一位进行平方相加运算后替换该数，再循环此过程，
# 当值为1时退出循环，return True，else return False
#需要用哈希表记录所有已出现过的数字，以检测是否进入了循环。

class Solution:
    def isHappy(self, n: int) -> bool:
        hash={}
        tempres=int()
        while n!=1 and n not in hash:
            hash[n]=1
#在哈希表中，键是唯一的。即使你多次尝试将相同的键添加到哈希表中，哈希表也只会保留一个实例。
            # 如果键已经存在，新的值会覆盖旧的值，但键的重复不会增加。
            tempres=0
            mlist=list(str(n))
            for m in mlist: #把m转换为int才可进行运算
                tempres+=int(m)**2
                n=tempres
        return n==1  # 如果 n 最终变成了 1，返回 True，否则返回 False

# 也可以用集合记录出现过的数字
hash_set = set()
        while n != 1 and n not in hash_set:
            hash_set.add(n)

#回顾解法：
class Solution:
    def isHappy(self, n: int) -> bool:
        hash={}
        while n not in hash and n!=1:
            hash[n]=1 #将当前的n加入hash检测循环
            res=0
            for num in list(str(n)):
                res+=int(num)**2
            n=res
        return n==1