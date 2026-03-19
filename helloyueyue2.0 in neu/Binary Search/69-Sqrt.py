#全闭区间
class Solution:
    def mySqrt(self, x: int) -> int:
        #[0,1,2,3,4,5,6,7,8] length = x + 1
        if x == 0:
            return 0
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        return r
        #r 是最后一个满足 mid*mid <= x 的值
        #l 是第一个满足 mid*mid > x 的值

#半闭区间
class Solution:
    def mySqrt(self, x: int) -> int:
        #[0,1,2,3,4,5,6,7,8] length = x + 1
        if x == 0:
            return 0
        l, r = 0, x + 1 #⚠️这里是x+1
        while l < r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid + 1
        return l - 1
