from collections import deque

#import sys
#sys.stdin = open('./input.txt', 'r')

# 1. 입력 받기
N, M = map(int, input().split())
B = []
for _ in range(N):
    B.append(list(input())) 
# tip! board = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]  # x축 움직임
dy = [0, 0, -1, 1]  # y축 움직임
q = deque()  # BFS : queue 활용
# Red(rx,ry)와 Blue(bx,by)의 탐사 여부 체크
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def move(x, y, dx, dy):
    cnt = 0  # 이동 칸 수
    # 다음이 벽(#)이거나 현재가 구멍(o)일 때까지 계속 움직임
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

# 2. bfs
def bfs():
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i, j
            elif B[i][j] == 'B':
                bx, by = i, j
    # 위치 정보와 depth(breadth 끝나면 +1)
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

    while q:  # BFS : queue 기준
        rx, ry, bx, by, answer = q.popleft() # answer : 구하려고 하는 가는 길의 거리
        if answer > 10:  # 실패 조건
            break
        for i in range(4):  
            # tip! 다음 좌표를 일단 부르고 조건으로 break하지 말고 함수를 하나 만듦
            # 각각 조건을 따져서 다음이 벽이 아니고 현재가 구멍이 아니면 +dx, +dy
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue

            # 파랑 구슬이 구멍에 안 빠졌을 때 
            # -> (1) 빨간 구슬만 구멍에 빠짐 / (2) 둘 다 구멍에 안 빠졌고 다른 구멍 / (3) 둘 다 구멍에 안 빠졌고 같은 구멍
            if B[nbx][nby] != 'O':  
                if B[nrx][nry] == 'O':  # (1) 성공
                    print(answer)
                    return
                if nrx == nbx and nry == nby:  # (3) 구슬 위치가 겹쳤을 때 
                    # -> *** 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 전으로 
                    if rcnt > bcnt:  
                        nrx -= dx[i]  
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
               
               # (2) 다른 구멍에 위치 -> 다음 움직임 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, answer+1))
    print(-1)  # 실패 시

bfs()
