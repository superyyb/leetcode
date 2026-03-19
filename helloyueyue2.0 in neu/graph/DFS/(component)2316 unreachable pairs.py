class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        '''
        这个一般般 看下面的复盘解法
        '''
        #edges
        #calculate the number and size of connected component(islands)连通分量
        count = 0
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [0] * n
        sizes = []
        def dfs(i):
            if visited[i]:
                return 0
            visited[i] = 1
            island_size = 1
            for j in g[i]:
                island_size += dfs(j)
            return island_size
        for i in range(n):
            size = dfs(i)
            sizes.append(size)
        total_sum = 0
        for i in range(n):
            total_sum += sizes[i] * (n - sizes[i])
        return total_sum // 2

    """
	•visited[i] = 1
这个操作只是做标记：表示“这个节点已经访问过了”。
它不会直接影响 dfs 的返回值，只是让下次遇到它时直接 return 0，避免重复计数和无限递归。
	•island_size = 1
这个才是让 dfs(i) 默认返回 至少 1 的原因。
意思是：当我第一次进入节点 i 时，就把“自己”算进去。
    """

#11.26复盘 一遍过👏
#类似695 max area of island 记得每次把area/size清零再算下一个component
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # count each size of components
        # Unreachable node pairs: size * (n - size)//2

        # Transfer edges to adjacent list
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)  # [[1, 2], [0, 2], [0, 1]]
        visited = [False] * n
        size = 0
        pairs = 0

        def dfs(i):
            nonlocal size
            # Base case
            if visited[i]:
                return
            # Mark the node as visited
            visited[i] = True
            size += 1
            for neighbor in g[i]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                size = 0#⚠️注意清零
                dfs(i)
                pairs += size * (n - size)
        return pairs // 2

#union find
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # calculate the size of each component
        # res = size * (n - size) // 2
        parent = [i for i in range(n)]
        def find(x):#return root - find the root of x
            if parent[x] != x:
                parent[x] = find(parent[x])
                #找出x所在集合的root，不管parent链有多长，让x直接挂在根上，让find(x) 变成 O(1)，查找节省时间
            return parent[x]
        def union(x, y):#return bool - try union and tell whether succeed
            rootX, rootY = find(x), find(y)
            if rootX == rootY:#产生环
                return False#但是对这道题来说 bool没有意义
            else:#合并
                parent[y] = rootX
        for u, v in edges:
            union(u, v)
        for i in range(n):
        #union之后有可能还存在重复的root，为了确保每个节点都直接指向最终 root，必须对每个 i 做一次 find(i)。
            find(i)
        dic = Counter(parent)
        seen = 0
        total = 0
        for num in dic.values():
            total += num * seen
            seen += num
        return total