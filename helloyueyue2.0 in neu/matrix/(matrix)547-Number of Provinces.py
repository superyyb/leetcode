class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #题目给了matrix 不需要自己构造图 直接遍历
        """
    从每个尚未访问的城市 i 出发做一次 DFS，
    把与 i 连到的一整块都标记为已访问。
    每触发一次新的 DFS，就说明发现了一个新的连通块,ans += 1。
        """
        n = len(isConnected) #matrix边长
        visited = [0] * n #visited[i]：城市i是否已经访问过
        ans = 0
        def dfs(i):#定义好访问城市的函数dfs()
            if visited[i]:#若i已被访问，直接返回
                return
            visited[i] = 1 #否则标记i为已访问
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    dfs(j)
    #dfs(i) 的作用是：找出以 i 为起点的整块“省份”，并把它们都标记为已访问。
        for i in range(n): #开始依次遍历每个城市
                if not visited[i]:
                    dfs(i)
                    ans += 1
        return ans