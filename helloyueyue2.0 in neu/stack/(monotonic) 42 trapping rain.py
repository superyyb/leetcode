class Solution:
    def trap(self, height: List[int]) -> int:
        #mono stack 遇到下一个相等或更大的元素就可以实现trap
        #原则：求左右两侧边界以及中间的bottom算出高度
        # right为此时for循环遍历的i，bottom为弹出的栈顶，left为弹出之后的栈顶
        #time/space: O(n)
        if not height:
            return 0
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:#we must calculate water everytime we pop a bottom
                    left = height[stack[-1]]
                    right = height[i]
                    h = min(right, left) - bottom
                    w = i - stack[-1] - 1
                    water += h * w
            stack.append(i) #把当前i入栈
        return water
    '''
单调栈的本质：所有元素一定都会至少入栈一次
无论它是否马上满足条件、是否会立刻被 pop——每个元素都会 “push 一次”
    '''

class Solution:
    def trap(self, height: List[int]) -> int:
        #two-pointer
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:#left decides the water
                water += left_max - height[left]
                left += 1
            else:#right decides the water
                water += right_max - height[right]
                right -= 1
        return water
        #for every index, we need to find:
        #left_max, right_max, height[i]
        #[5,0,0,2,7,2]

