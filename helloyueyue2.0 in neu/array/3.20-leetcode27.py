#快慢指针
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i=0
        j=0#记录不等于val的元素
        while i<len(nums):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
            i+=1
        return j
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
"""
def main():
    nums = [0,1,2, 2, 3, 0,4,2]
    val = 2
    sol=Solution()
    print(sol.removeElement(nums,val))

if __name__=="__main__":
    main()

