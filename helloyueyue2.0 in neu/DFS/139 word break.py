'''
dfs用来从头到尾遍历每一个start
for loop用来遍历每一个start对应的每个end

0   1   2   3   4   5   6   7   8
|   l   e   e   t   c   o   d   e   |
↑                                   ↑
start=0                          start=8（到终点了）
所以最后一个切割点：start == len(s)
'''
'''
1. 什么时候停 →  start == len(s) 说明拆完了
2. 当前在哪  →  start 位置
3. 能往哪走  →  尝试每个 end，s[start:end] 在字典里就往下走
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #Use dfs to search whether s[start:end] is in wordDict
        memo = {}
        words = set(wordDict) # 优化查询速度
        def dfs(start):
            if start == len(s):
                return True
            if start in memo: # 查表
                return memo[start]
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:#s[start:end] 解决的是"当前这段"，
                    if dfs(end):#dfs(end)解决的是"剩下那段"，两个都要为 True 才算成功。
                        memo[start] = True#能走通，记账
                        return True
            #只有当上面的 for 循环跑完了，说明尝试了所有 end 都不行
            # 这时候才能确定这个 start 是失败的
            memo[start] = False#不能走通，记账
            return False
        return dfs(0)