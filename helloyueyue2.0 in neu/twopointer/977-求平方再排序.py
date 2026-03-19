class Solution:#偷懒方法用sorted()
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums: #[-4,-1,0,3,10]
            num = num*num #[16,1,0,9,100]
            res.append(num)
        return sorted(res)

#双指针
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    #先用双指针将其绝对值排序，从后往前排，再统一平方 [-4,-1,0,3,10]
    #non-decreasing: 绝对值最大的元素一定在两端，每次从两端中挑出绝对值更大的那个
        n = len(nums)
        res = [0]*n
        res_index = n - 1
        i, j = 0, n - 1
        while i <= j:#如果用i < j，在循环结束后要把res[0]赋值，循环不会处理最后那个元素
            if abs(nums[i]) > abs(nums[j]):
                res[res_index] = nums[i]*nums[i]
                i += 1
            else:
                res[res_index] = nums[j]*nums[j]
                j -= 1
            res_index -= 1
        #res[0] = nums[j]*nums[j]
        return res