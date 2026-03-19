#写在前面：这种题要学会用max()函数和如何覆盖刷新值

#答案1：预设一个数组存储1的个数，通过max(counts)取到最大值
# 当遇到1时：tmp_count ++
# 当遇到0时：说明连续的1已经被打断，此时记录已经收集到的1的个数，同时将tmp_count归零
# 当遍历到末尾的时候，直接append当前的tmp_count值，因为在遍历到1的时候无法立刻使用append将值写入到count中1
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=[]
        temp_count=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp_count+=1
            elif nums[i]==0:
                count.append(temp_count)
                temp_count=0 #重置temp_count
            if i==len(nums)-1:
                count.append(temp_count)
        return max(count)

#优化：
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        temp_count = 0
        for num in nums:
            if num == 1:
                temp_count += 1
            else:
                # 更新最大连续1的个数，并重置temp_count
                max_count = max(max_count, temp_count)
                temp_count = 0
        # 最后一次检查，处理末尾是1的情况
        max_count = max(max_count, temp_count)
        return max_count

