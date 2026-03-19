"""
What you really want is to keep looping until either:
	1.	n becomes 1 (happy),
	2.	or you see a repeat (unhappy).

Then, after the loop finishes, you return whether you ended at 1:
"""
class Solution(object):
    def isHappy(self,n:int)->bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n_str=str(n)
            res=0
            for i in range(len(n_str)):
                pre=int(n_str[i])**2
                res=res+pre
            n=res
        if n==1:
            return True
        else:
            return False

def main():
    sol=Solution()
    num=sol.isHappy(19)
    print(num)
if __name__=="__main__":
    main()