class Solution:#O(√c)
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(c ** 0.5)
        while i <= j:
            if i*i + j*j == c:
                return True
            elif i*i + j*j > c:
                j -= 1
            else:
                i += 1
        return False

class Solution:#O(√clogc)
    def judgeSquareSum(self, c: int) -> bool:
        def BinarySearch(n:int) -> bool:
            l, r = 0, n #0,1,2,3,4
            while l <= r:
                mid = l + (r - l)//2
                if mid * mid == n:
                    return True
                elif mid * mid < n:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        for i in range(0,int(c**0.5)+1):
            n = c - i*i
            if BinarySearch(n):
                return True
        return False