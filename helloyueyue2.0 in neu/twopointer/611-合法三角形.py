class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0 #两边之和大于第三边，固定最大边为k，双指针分别对应另外两条边
        for k in range(len(nums) - 1, 1, -1):#range(start,stop,step)不包括stop，所以不包含1，实际是到2结束的
            a, b = 0, k - 1
            while a < b:
                if nums[k] < nums[a] + nums[b]:
                    count += b - a
                    b -= 1
                else:
                    a +=1
        return count

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 两边之和大于第三边 选取最大的数字作为第三边，如果两边之和比他大，那么肯定比剩下的数字都大
        count = 0
        nums.sort()
        for k in range(2, len(nums)):  # k从2开始，因为第一次循环i=0，j=1
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
"""
主流写法还是k从大到小判断，先枚举k最大值（最大边）
range(2, len(nums)) 等同于 range(len(nums)-1，1，-1)

        nums[i] <= nums[i+1] <= ... <= nums[j]
        if 
            nums[i] + nums[j] > nums[k]
        then:
            nums[i+1] + nums[j] > nums[k]
            nums[i+2] + nums[j] > nums[k]
            ...
            nums[j-1] + nums[j] > nums[k]
"""

