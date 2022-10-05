from collections import deque
def bfs(start_node, visited, w): 
    #start_node와 node의 연결을 끊었을 때의 한쪽 송전탑 개수
    q = deque()
    q.append(start_node) # q= deque([start_node])로 한 줄로 작성 가능
    visited[start_node] = True
    num = 1 # 리턴할 송전탑 개수
    
    while q:
        x = q.popleft()
        for i in w[x]: #x와 연결된 노드에 관해서
            if visited[i] == False: # 방문 안한 애들 방문
                visited[i] = True
                num += 1
                q.append(i)
    return num

def solution(n, wires):
    # input: 송전탑(node) 개수 n, 전선 정보 wires(2d list)
    # ouput: 송전탑을 두 전력망으로 나눴을 때 두 개의 송전탑 개수 차이 최솟값
    
    # idea: 각 wire를 끊었을 때 값 일일이 비교 -> 완전 탐색
    # issue: 이어진 전선 개수 구하는 법 -> bfs
    w = [[] for _ in range(n+1)] #
    for wire1, wire2 in wires: # tip: for wire in wires라고 하고 wire[0], wire[1] 말고
        w[wire1].append(wire2) # w[a][b]=1 / a와 b연결되어 있음 대신에
        w[wire2].append(wire1) # w[wire1][wire2] = 1, w[wire2][wire1] = 1
        
    # wires에서 각 wire 끊어보기
    answer = n
    for start_node, node in wires: # tip: 이 문제의 경우 2중 for문 할 필요 없음
        visited = [False]*(n+1) # 방문 여부 체크
        visited[node] = True
        num = bfs(start_node, visited, w) #start_node와 node 끊었을 때의 한쪽 송전탑 개수
        if abs(num - (n-num)) < answer:
            answer = abs(num-(n-num))
    return answer