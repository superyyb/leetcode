#9.8复盘
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 每到一个台阶，判断离终点距离，如果还不够，那么再找更大的跳跃步数，如果够了 直接到终点
        if len(nums) <= 1:
            return 0
        count = 0
        j, next_j = 0, 0 #j为当前一跳可覆盖的范围，next_j为下一跳可覆盖的范围
        for i in range(len(nums) - 1):#最后一步不用跳了
            next_j = max(next_j, i + nums[i])
            if i == j:
                count += 1
                j = next_j
                if j >= len(nums) - 1:
                    return count

#Jan6复盘
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
    1.Find the farthest distance every jump can get
    2.Compare with the total jumps, if farthest distance >= total, return answer
    3.If still don't get to the final, add 1 to answer
        '''
        ans = 0
        farthest = 0  # 当前层范围内，下一次能跳到的最远下标
        end = 0  # 当前层的右边界
        n = len(nums)
        if n <= 1:
            return ans
        for i in range(n - 1):
            farthest = max(farthest, nums[i] + i)
            if farthest >= n - 1:
                ans += 1#⚠️为什么这里还要+1，虽然知道下一步就能到终点，但是还没把下一步计入答案
                break
            if i == end:  # 当前层已经走完了 但是还没完成任务
                ans += 1
                end = farthest
        return ans


