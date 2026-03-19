class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len((numbers))):
            for j in range(i+1,len((numbers))):
                #key:or I will get the same index [1,1] for [0,0,11,15]
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash={}
        for i,num in enumerate(numbers):
            if num not in hash:
                hash[num]=1
        if target-num in hash:
            return [i+1,]




if __name__=="__main__":
    sol=Solution()
    print(sol.twoSum([0,0,11,15],0))
