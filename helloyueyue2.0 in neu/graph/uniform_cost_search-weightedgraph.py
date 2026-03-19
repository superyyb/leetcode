import heapq
def uniform_cost_search(graph,start,goal,path=None):
    if path==None:
        path=[start]
    pq=[(0,start,path)]
    #use a tuple to record current cost,current node and path
    visited= {}#to record the lowest cost so far
    while pq:
        cost,node,path=heapq.heappop(pq)
        if node in visited and visited[node]>cost:
            continue
        visited[node]=cost
        if node==goal:
            return path,cost
        for (neighbor,weight) in graph.get(node,[]):
            new_cost=cost+weight
            path+=[neighbor]
            pq.append(new_cost,neighbor,path)
    return None




"""
      (A)
     /   \
  1 /     \ 4
   /       \
 (B)---2---(C)
   \       /
  5 \     / 1
     \   /
      (D)
weighed graph:use a dictionary
"""
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
        }