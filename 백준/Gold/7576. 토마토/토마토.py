'''
N*M 토마토 칸(토마토 없을 수도)
익은 토마토는 양 옆 네 개에 영향을 준다(대각선 X)
며칠이면 다 익게 되는 지 최소 일수를 구하라
1: 익음 / 0:익지 않음 / -1: 토마토 없음
'''
from collections import deque
#import sys
#sys.stdin = open('./input.txt', 'r')

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
#print(arr)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

def bfs():
    while q:
        x, y = q.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1 # cnt -> 이전 값 +1 하면 몇번째인지 저장 가능
                    q.append([nx, ny])
    return 

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: # 1이 여러 개일때 횟수 세기 -> q에는 첫번째 방문하는 좌표가 담긴다는 걸 명심!
            q.append([i, j])
#print(q)
bfs()
#print(arr)
# '1'로 가득찼는지도 일단 bfs 끝난 결과로 판별
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0) #더 이상 뒤로 실행 안되게
    cnt = max(cnt, max(i)) # *전체 중 max 값 이렇게 표시
print(cnt-1)

