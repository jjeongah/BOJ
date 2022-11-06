from collections import deque

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    fx, fy = pos[0]
    bx, by = pos[1]
    
    # 상하좌우 탐색
    for dx, dy in dirs:
        nfx, nfy = fx + dx, fy + dy
        nbx, nby = bx + dx, by + dy
        if board[nfx][nfy] == board[nbx][nby] == 0:
            next_pos.append({(nfx, nfy), (nbx, nby)})
    
    # 가로로 놓여있을 때
    if fx == bx:
        # 아래쪽으로 회전하는 경우 아래 두 칸에 벽이 없어야함
        # 위쪽으로 회전하는 경우 위 두 칸에 벽이 없어야함
        for i in [1, -1]:
            if board[fx+i][fy] == board[bx+i][by] == 0:
                next_pos.append({(fx, fy), (fx+i, fy)})
                next_pos.append({(bx, by), (bx+i, by)})
    
    # 세로로 놓여있을 때
    elif fy == by:
        # 오른쪽으로 회전하는 경우 오른쪽 두 칸에 벽이 없어야함
        # 왼쪽으로 회전하는 경우 왼쪽 두 칸에 벽이 없어야함
        for i in [1, -1]:
            if board[fx][fy+i] == board[bx][by+i] == 0:
                next_pos.append({(fx, fy), (fx, fy+i)})
                next_pos.append({(bx, by), (bx, by+i)})
    
    return next_pos

def solution(board):
    answer = 0
    
    # 기존 맵에 외각 만들기 → 로봇이 맵을 벗어나는지 아닌지 쉽게 판정하기 위해
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # 위치 저장 저장
    ## {} (집합 자료형)으로 관리할 경우 {(1,1), (1,2)} 과 {(1,2),(1,1)}은 같기 때문에 중복 방지
    q = deque([({(1,1), (1,2)}, 0)])
    visited = []
    
    while q:
        pos, cnt = q.popleft()
        # 도착한 경우 종료
        if (n, n) in pos:
            return cnt
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                q.append((next_pos, cnt+1))
        
    return answer