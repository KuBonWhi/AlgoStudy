# # 크루스칼
# def getParent(parent, x):
#     if parent[x] != x:
#         parent[x] = getParent(parent, parent[x])
#     return parent[x]

# def unionParent(parent, a, b):
#     a = getParent(parent, a)
#     b = getParent(parent, b)
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def solution(n, costs):
#     answer = 0
#     parent = [i for i in range(n)]
#     costs.sort(key = lambda x:x[2])
#     print(costs)
#     print(parent)
    
#     for start, end, cost in costs:
#         if getParent(parent, start) != getParent(parent, end):
#             unionParent(parent, start, end)
#             answer += cost
    
    
#     return answer

# prim
import heapq

def prim(start, n, graph):
    visited = [False for _ in range(n)]
    queue = []
    heapq.heappush(queue, [0, start])
    totalCost = 0
    
    while queue:
        cost, v = heapq.heappop(queue)
        if not visited[v]:
            visited[v] = True
            totalCost += cost
            
            for nextV, nextCost in graph[v]:
                if not visited[nextV]:
                    heapq.heappush(queue, [nextCost, nextV])
    
    return totalCost
            

def solution(n, costs):
    answer = 0
    graph = [[] for i in range(n)]
    
    for start, end, cost in costs:
        graph[start].append([end, cost])
        graph[end].append([start, cost])

    answer = prim(0, n, graph)
        
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))