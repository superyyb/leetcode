class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        mid=len(nums)//2
        if target==nums[mid]:#terminate condition
            return mid
        if target>nums[mid]:
            return self.search(nums[mid+1:],target)
        else:
            return self.search(nums[:mid],target)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            if nums[mid] < target:
                i=mid+1
            else:
                j=mid-1
        return -1
if __name__=="__main__":
    sol=Solution()
    print(sol.search([-1,0,3,5,9,12],9))