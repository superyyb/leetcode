class Solution:#暴力法 O(n2)
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 2):
                if nums[i] == nums[j]:
                    return nums[i]

class Solution:#快慢指针
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:#用来判断slow，fast是否相遇，一旦相遇break循环
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]#重置slow位置
        while slow != fast:#用来判断再次相遇的位置
            slow = nums[slow]
            fast = nums[fast]
        return slow
    """
    •关键定理：当第一次相遇后，把其中一个指针移回“起点”，然后两个指针都改成“每次走 1 步”，
     它们下一次相遇的位置就是 环的入口。在这个题里，“环的入口”正对应 重复的数字。
	
    为什么要根据 nums[i] 的值来跳转，这样才能形成链表结构，找到那个重复值构成的环
    nums = [1, 3, 4, 2, 2]
      index:0, 1, 2, 3, 4
    0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 -> ...重复的是index2和index4
    因为你有 n + 1 个点，却只能跳到 n 个地方去，跳着跳着就一定会走回头路形成一个环。
    """

class Solution:#集合去重❌题目只允许constant extra space
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


class Solution:#BinarySearch
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        ans = -1
        while l <= r:
            count = 0
            mid = l + (r - l) // 2
            left_nums, right_nums = 0, 0
            for num in nums:
                if num < mid:
                    count += 1
            if count > mid:
                l = mid + 1
                ans = mid
            else:

                r = mid - 1
        return ans

    """
    [1,1,4,2,3]
    l=1,r=4 1,2,3,4 mid = 2 <=2的有3个，所以重复值一定在[1...2]中
    """