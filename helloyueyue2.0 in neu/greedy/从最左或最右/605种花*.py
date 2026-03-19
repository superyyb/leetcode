class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        #什么情况可以种花：首尾有两个0或中间有三个0
        #对于每个位置 i，只有当前为 0，且左右都是 0（或者是边界），才能种花
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1 #种花
                    n -= 1
                    if n == 0:
                        return True
                    i += 2 #跳过当前已种花位置
                    continue #如果执行了continue，那么会跳过本次循环的i += 1，直接进入下一次循环
            i += 1
        return n == 0