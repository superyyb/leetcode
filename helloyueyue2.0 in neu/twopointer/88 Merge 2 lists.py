class Solution:#偷懒用sort
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #构造nums1虚拟长度(m+n)  [1,2,3,0,0,0],[0,5,6]
        length_nums1 = m + n
        i = m
        for j in range(n):
            nums1[i] = nums2[j]
            i += 1
        nums1.sort()


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
    题目提示nums1末尾有空位，因此我们从后往前填充是安全的，不会覆盖nums1原本元素
        """
        #  [1,2,3,5,8,0,0,0] [2,5,6]
        p1, p2, p = m - 1, n - 1, m + n - 1  # p1:nums1,p2:nums2 p:res_nums1
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            elif nums2[p2] <= nums1[p1]:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        # 如果nums2有剩余（不存在nums2还有元素比nums1小，因为前面while循环已经比较过了，遍历了所有nums1元素 把大的都插到后面了，因此到现在为止nums2的元素都比nums1小）
        # 如果nums1有剩余，nums1剩下的元素本来就比nums2小，并且已经排好序，不用再处理
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1


