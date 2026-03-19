class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        count = 0
        for char in list(s):
            freq[char] = freq.get(char, 0) + 1
        cnts = sorted(freq.values(), reverse = True)
        prev = cnts[0]
        for c in cnts[1:]:
            target = min(c, prev - 1)#本轮的target最多能保留 prev−1，但不能低于 0
            if target < 0:
                target = 0
            count += c - target #当前频次减去target为需删减的数量
            prev = target
        return count

#用set找到unique的freq，这种写法不需要对freq做排序处理
class Solution:
    def minDeletions(self, s: str) -> int:
        S = Counter(s)
        unique = set()
        count = 0
        for char, freq in S.items():
            while freq > 0 and freq in unique:
                freq -= 1
                count += 1
            unique.add(freq)
        return count
