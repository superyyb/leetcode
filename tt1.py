def solution(str):#O(n2)
    res = ""
    vowels = {"a", "e", "i","o","u"}
    j = len(str) - 1
    while j >= 0:
        if str[j].lower() not in vowels:#注意大小写
            res += str[j]
        j -= 1
    return res

def solution(s): #O(n)
    vowels = {"a", "e", "i", "o", "u"}
    res = []
    for ch in reversed(s):
        if ch.lower() not in vowels:
            res.append(ch)
    return "".join(res)   # O(n) 一次性拼接

if __name__ == "__main__":
    str = "Hello, world!"
    res = solution(str)
    print(res)
