class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            if arr[mid] > arr[mid+1]:
                r = mid
        return r#或者return l
    #为什么mid+1不会越界：在循环中，一定有 l < r → mid < r，因此mid + 1 ≤ r ≤ len(arr) - 1

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
    #因为mid向左取整，而[l,r]是全闭区间，因此肯定存在mid+1，不会出现list out of range的情况
            if arr[mid] <= arr[mid+1]:
                l = mid + 1
            if arr[mid] > arr[mid+1]:
                r = mid - 1
        return l
'''
为什么852只能mid和mid+1比较，但162可以与mid-1比较
对比点	                 162                	852
数组类型	        任意起伏，无全局单调性	           单峰单调结构
可以比较哪边	    左边或右边都行（峰有多个）	       只能右边（峰唯一）
区间不变性	    只要朝上坡方向走就行	        必须保持区间包含唯一峰
越界风险	        可加条件 mid > 0            	需要访问 mid+1，无越界
'''