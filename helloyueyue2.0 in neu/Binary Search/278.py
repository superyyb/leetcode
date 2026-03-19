# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            res = isBadVersion(mid)
            if res is True and isBadVersion(mid-1) is False:
                return mid
            if res is True:
                r = mid - 1 #往左
            elif res is False:
                l = mid + 1 #往右

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid - 1
            elif not isBadVersion(mid):
                l = mid + 1
        return l