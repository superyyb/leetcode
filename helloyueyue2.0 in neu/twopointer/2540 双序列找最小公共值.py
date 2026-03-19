class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """
        双序列双指针：找到同时出现在两个序列中的最小的元素
        [1,2,3,6]
        [2,3,4,5]
        """
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            #必须确保两个索引都没有越界，否则会报错。
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        return -1

class Solution:#用集合找重复值
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        visited = set()
        for num in nums1:
            if num not in visited:
                visited.add(num)
        for num in nums2:
            if num in visited:
                return num
        return -1