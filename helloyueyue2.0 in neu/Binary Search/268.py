class Solution: #time:O(n)、extra space:O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums) #O(1)
        total = n * (n + 1) // 2 #O(1)
        return total - sum(nums) #调用sum函数：O(n) 遍历整个列表，对每个元素进行一次加法

class Solution:# half-open interval[) time:O(nlogn）、extra space:O(1)/O(n)
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        #nums.sort()：modifies original list，method of the list object (list), and can only be called on lists
        #nums=sorted(nums) is a built-in global function 返回新的列表 需要O(n)额外空间
        #用的都是同一套 O(n log n) 最坏情况、O(n) 最好情况的 Timsort。
        # [0,8] mid=4 nums[mid]=4
        # [5,8] mid=6 nums[mid]=6
        # [7,8] mid=7 nums[mid]=7
        # [8,8] mid=8 nums[mid]=9
        # r=8 l=8退出循环
        l,r = 0, len(nums)#有可能n为缺失值
        while l<r:#二分  O(log n)
            mid=l+(r-l)//2
            if nums[mid] > mid:
                r = mid
            if nums[mid] == mid:#或者用else:
                l= mid + 1
        return l#第一个不满足 r 最小的满足

class Solution:#closed interval time：O(nlogn) space：O(1)
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        """
    nums:[0,1,2,3,4,5,6,7,9] len(nums)=9
    index:0,1,2,3,4,5,6,7,8
        """
        #[0,8] mid=4 nums[mid]=4
        #[5,8] mid=6 nums[mid]=6
        #[7,8] mid=7 nums[mid]=7
        #[8,8] mid=8 nums[mid]=9
        #r=7 l=8退出循环
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] > mid:
                r = mid - 1 #有可能mid是我们要找的，或者在mid左侧
            if nums[mid] == mid:#或者else: mid不是我们要找的答案，答案一定在右边
                l = mid + 1
    #退出循环时，l=r+1 ，本来最后一次循环他们都指向最后一个对齐的数，r 指向最后一个nums[mid] == mid，l 则指向第一个「不对齐」的下标
        return l
    """
[0,1,2,3,4,5,7]  
[0,1,2,3,4,5]
[0,1,3,4,5]
    """
class Solution:#hash/set time：O(n) space：O(n)
    def missingNumber(self, nums: list[int]) -> int:
        s=set(nums)
        for i in range(len(nums)+1):
            if i not in s:
                return i
#set(nums) 会对 nums 中的 n 个元素做一次哈希插入， O(n)。
#随后for循环 i 从 0 到 n，共 n+1 次，每次 i not in seen 在哈希表中查找， O(n)。
#空间复杂度：需要额外的 seen 集合来存放原数组的所有元素，一共 n 个整数 → O(n)。

class Solution:#time:O(n) space:O(n)
    def missingNumber(self, nums: list[int]) -> int:
        hash={}
        for num in nums:#O(n)
            if num not in hash:
                hash[num]=1
        for i in range(len(nums)+1):#O(n)
            if i not in hash:
                return i
