#My solution
class Solution:
    def minimumMoves(self, s: str) -> int:
        move = 0
        s = list(s)
        for i in range(len(s) - 2):
            if s[i] == "X":
                s[i] = "0"
                s[i + 1] = "0"
                s[i + 2] = "0"
                move += 1
        if s[-1] == "X" or s[-2] == "X":
            move += 1
        return move

#More elegant；这样就不用改变数组的值了 仅计算move就可以
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s):
            if s[i] == "X":
                ans += 1
                i += 3
            else: i += 1
        return ans