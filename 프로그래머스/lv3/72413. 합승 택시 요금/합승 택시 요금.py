import heapq

def dijkstra(graph, n, start, end):
    q = []
    heapq.heappush(q, [0, start]) # 시작 노드 정보 삽입 [길이, 노드] / 길이 기준으로 pop해야 하니까 길이 먼저
    
    INF = float('inf')
    distance = [INF]*(n+1) # 노드 번호별로 거리 기록
    distance[start] = 0 # 시작노드 -> 시작 노드 거리 기록
    
    while q:
        dist, node = heapq.heappop(q) # 그 노드까지의 거리, 다음 갈 수 있는 노드 
        if distance[node] < dist: # 뽑은 거리가 더 크면 방문한 셈치고 무시
            continue
        for next_node, next_cost in graph[node]: # 다음 갈 수 있는 노드에 도착. 그 다음 노드 찾기
            cost = distance[node] + next_cost # (시작-> node 의 거리) + (node -> node의 인접 노드 거리)
            if cost < distance[next_node]: 
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                
    return distance[end]

def solution(n, s, a, b, fares):
    '''
    <input>
    n: 지점의 개수
    s: 출발지점
    a: A의 도착 지점
    b: B의 도착 지점 (a!=b)
    fares: 지점 사이의 예상 택시 요금 / [[c,d,f]] c와 d 지점 사이의 요금은 f
    
    <output>
    s에서 도착 지점까지 택시 탈 때 최저 예상 택시 요금 계산해서 return
    * 합승 꼭 안해도 됨
    
    <idea>
    * 다익스트라: 방문하지 않는 노드 중 최단 거리가 가장 작은 노드를 돌아가며 선택
    '''
    graph = [[] for _ in range(n+1)] #인접행렬
    
    for fare in fares:
        node1, node2, cost = fare
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))
    
    # 1. 합승 안하는 경우
    not_together = dijkstra(graph, n, s, a) + dijkstra(graph, n, s,b) 
    
    # 2. 합승 하는 경우
    # 어디까지 같이 타고 갈까? (출발지 아닌) 지점을 전부 가보면서 최솟값 갱신
    money = 99999999
    for i in range(1, n+1): # 0~n-1이 아닌 1~n
        if i != s:
            money = min(money, dijkstra(graph, n, s, i) + dijkstra(graph, n, i, a) + dijkstra(graph, n, i, b))
            
    return min(not_together, money)