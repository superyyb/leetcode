class Solution:
    def isHappy(self, n: int) -> bool:
        hash={}
        while True:
            sum = 0
            for i in str(n):
                sum+=int(i)**2
            if sum==1:
                return True
            if sum in hash:
                return False
            hash[sum]=1
            n=sum


if __name__=="__main__":
    n=19
    sol=Solution()
    print(sol.isHappy(n))
