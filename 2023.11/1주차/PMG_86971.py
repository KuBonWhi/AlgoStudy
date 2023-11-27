from collections import deque
from copy import deepcopy

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = False
    cnt = 0 

    while queue:
        now = queue.popleft()
        cnt+=1
        for next in graph[now]:
            if visited[next]:
                queue.append(next)
                visited[next] = False
    
    return cnt


def solution(n, wires):
    answer = []

    for wire in wires:
        graph = [[] for i in range(n+1)]
        visited = [True for i in range(n+1)]
        copyWires = deque(wires)
        copyWires.remove(wire)

        for [start, end] in copyWires:
            graph[start].append(end)
            graph[end].append(start)
        
        cnt1 = bfs(wire[0], graph, visited)
        cnt2 = bfs(wire[1], graph, visited)
        # print(wire, cnt1, cnt2)
        answer.append(abs(cnt1-cnt2))
    
    print(answer)
        
    return min(answer)








print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))