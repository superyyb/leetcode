# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            ans= guess(mid)
            if ans == 0:
                return mid
            elif ans == -1: #guess is too high
                r = mid - 1
            elif ans == 1: #guess is too low
                l = mid + 1