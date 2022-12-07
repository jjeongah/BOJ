'''
1. dest에서 출발
2. 결과 list를 -1로 선언해두고 +1씩
3. visited 기록을 위해서 list가 아닌 set 사용
'''
from collections import deque    
        
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)] # 인접 리스트
    for road in roads:
        a, b = road[0], road[1]
        graph[a].append(b)
        graph[b].append(a)
    # print(nodes)
    
    des = [-1 for _ in range(n+1)]
    des[destination] = 0
    Q = deque([destination])
    visited = set([destination]) # 원소 중복 없이 add하려고 집합 사용
    while Q:
        node = Q.popleft()
        for x in graph[node]:
            if x not in visited:
                visited.add(x)
                des[x] = des[node]+1
                Q.append(x)
                
    return list(des[s] for s in sources)