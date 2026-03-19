class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        不要用可变的 set 作为字典 key；
        改成不可变的 tuple就能既忽略顺序，又可以哈希。
        """
        seen = {}
        count = 0
        for i, domin in enumerate(dominoes):
            domin = tuple(sorted(domin))#用sorted把乱序统一
            count += seen.get(domin, 0)
            seen[domin] = seen.get(domin, 0) + 1
        return count

    """
    或者：
    count = 0
    for v in seen.values():
        count += v * (v - 1) // 2
    return count #类似leetcode1512
    """