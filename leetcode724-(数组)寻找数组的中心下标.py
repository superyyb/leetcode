#yy思路：len(nums)=i nums[i-1]为最后一个元素
#先算出总和，%2即为需要相等的和 (没必要 中间漏了一个数) 双指针 i在前j在后 直到两个相等 输出i
'''
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        #sum_total=sum(nums) #用sum()求列表元素和
        i,j=0,len(nums)-1
        sum_left,sum_right=0,0
        while i<j:
            if sum_left!=sum_right!=0:
                sum_left+=nums[i]
                sum_right+=nums[j]
                i+=1
                j-=1
        return i
不要执着于找相等，换个思路：左边的不够加左边的 else：加右边的
'''

'''
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        #sum_total=sum(nums) #用sum()求列表元素和
        i,j=0,len(nums)-1
        sum_left,sum_right=0,0
        while i<j:
            if sum_left<sum_right:
                sum_left+=nums[i]
                i+=1
            else:
                sum_right+=nums[j]
                j-=1
            if sum_left==sum_right:
                return i
        return -1
也错了，对于[-1,-1,-1,-1,-1,0]无法实现，双指针有时候无法同步到达正确的平衡点
'''

#单指针一次遍历从：左边=总-右边-num[i]
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        #sum_total=sum(nums) #用sum()求列表元素和
        i=0
        sum_total = sum(nums)
        sum_left=0
        while i<len(nums):
            sum_right=sum_total-sum_left-nums[i]
            if sum_left==sum_right:
                return i
            sum_left+=nums[i]
            i+=1
        return -1

#大神思路：同样是判断左右和相等，直接将右边的设为sum(nums)，每判断一次右边减num[i]，左边加num[i]
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left, sum_right = 0, sum(nums)
        for i in range(len(nums)):
            sum_right -= nums[i]
            # 若左侧元素和等于右侧元素和，返回中心下标 i
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
        return -1


