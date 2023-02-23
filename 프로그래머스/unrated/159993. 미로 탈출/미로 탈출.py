'''
통로로 된 칸(O) 나가려면 레버 필요
출발 지점(S) -> 레버(L)가 있는 칸 (레버 당긴 후) -> 미로 빠져 나옴(E)
레버 안 당겨도 출구 있는 칸 '지나갈 수' 있음
한 칸 이동 1초, 최대한 빠르게 미로를 빠져나가는 데 걸리는 시간은? (탈출 못하면 -1)

bfs
idea: *레버 어떻게 처리? => 레버로 가는 로직 + 레버에서 도착점으로
*visit 어떻게 체크? => 
*cnt 어떻게 계산? => 별도의 리스트 사용

from collections import deque
def solution(maps):
    arr = []
    for map in maps:
        arr.append(list(map))
    row = len(arr)
    col = len(arr[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 1. 어디가 시작인지 먼저 찾기
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 'S':
                sx, sy = i, j
                
    def bfs(x, y, end):
        q= deque()
        q.append([x,y])
        visited = [[-1]*col for _ in range(row)]
        visited[x][y] = 0
        
        while q:
            x, y = q.popleft()
            if arr[x][y] == end:
                return [visited[x][y], x, y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0<= nx < row) and (0<= ny < col):
                    if visited[nx][ny] == -1:
                        if arr[nx][ny] != 'X': # 'O'인지 'L'인지 따질 필요 X
                            q.append([nx, ny])
                            visited[nx][ny] = visited[x][y]+1 #visited 표시
        return None
    
    cnt = bfs(sx, sy, 'L')
    if cnt == None:
        return -1
    answer = cnt[0]
    cnt = bfs(cnt[1], cnt[2], 'E')
    if cnt == None:
        retrun -1
    answer += cnt[0]          
    return answer
'''
from collections import deque
def solution(maps):
    answer = 0
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    n,m = len(maps),len(maps[0])
    # 출발 지점
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx,sy = i,j
    # 레버 찾기
    def bfs(x,y,end):
        q = deque()
        q.append([x,y])
        visited = [[-1]*m for _ in range(n)]
        visited[x][y] = 0
        while q:
            x,y = q.popleft()
            if maps[x][y] == end:
                return [visited[x][y],x,y]
            for dir in direction:
                nx = x + dir[0]
                ny = y + dir[1]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == -1:
                        if maps[nx][ny] != 'X':
                            q.append([nx,ny])
                            visited[nx][ny] = visited[x][y] + 1
        return None
    cnt = bfs(sx,sy,'L')
    if cnt == None:
        return -1
    answer += cnt[0]
    cnt = bfs(cnt[1],cnt[2],'E')
    if cnt == None:
        return -1
    answer += cnt[0]
    return answer