class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]:#左边有序
                if nums[mid] > target >= nums[l]:#⚠️一定不能少target >= nums[l],加=符合全闭区间
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:#右边有序 或直接写else:
                if nums[mid] < target <= nums[r]:#⚠️一定不能少target <= nums[r]，边界要完整
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
