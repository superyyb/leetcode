class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        hash={}
        list=[]
        for num in nums:
            if num in hash:
                hash[num]+=1
            else:
                hash[num]=1
        for item in hash:
            if hash[item]==2:
                list.append(item)
        return list

if __name__=="__main__":
    sol=Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1,8]
    print(sol.findDuplicates(nums))

