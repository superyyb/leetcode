class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        list1 = [ord(c) - ord('a') for c in s1]
        list2 = [ord(c) - ord('a') for c in s2]
        list1.sort()
        list2.sort()
        can1 = True  # 假设 s1 可以 break s2
        can2 = True  # 假设 s2 可以 break s1
        for x, y in zip(list1, list2):
            if x < y:
                can1 = False
            if y < x:
                can2 = False
            if not can1 and not can2:
                return False
        return can1 or can2

#其实字符串里字母本身也可以排序 不需要转为数字
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        can1 = can2 = True
        for i in range(len(s1)):
            if(s1[i] < s2[i]):
                can1 = False
            elif(s1[i] > s2[i]):
                can2 = False
            if not can1 and not can2:
                return False
        return can1 or can2