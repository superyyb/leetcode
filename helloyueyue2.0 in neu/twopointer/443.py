"""
⚠️经常犯的错：while永远出不去，死循环
write = 0
        for i in range(1, len(chars)):
            while chars[i] == chars[i - 1]:
                j += 1
            chars[j] = j
            j = 0
"""
