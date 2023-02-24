import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
# 1. 인접행렬로 노드 간 연결 저장
graph = [[0] * (N + 1) for _ in range(N + 1)]  
for _ in range(M):
  node1, node2 = map(int, input().split())
  graph[node1][node2] = 1
  graph[node2][node1] = 1

  def bfs(V):
    # 3. 처음 방문 값 큐에 저장
    q = deque()
    q.append(V)
    bfs_visited[V] = 1 # 방문 여부 업데이트하는 거 잊지 말기
    while q:
      V = q.popleft() 
      print(V, end=" ")
      for i in range(1, N + 1): # 큐에 저장된 값 pop한 후 연결된 애들 확인
        if bfs_visited[i] == 0 and graph[V][i] == 1:
          q.append(i)
          bfs_visited[i] = 1
          
  def dfs(V):
    dfs_visited[V] = 1
    print(V, end=" ")
    for i in range(1, N+1):
      if dfs_visited[i] == 0 and graph[V][i] == 1:
        dfs(i)

# 2. 각 노드 간 방문 여부를 저장하는 리스트
bfs_visited = [0] * (N + 1)
dfs_visited = [0] * (N + 1)
dfs(V)
print()
bfs(V)
