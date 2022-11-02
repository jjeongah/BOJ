from copy import deepcopy 
# !! deepcopy 사용 이유: 여러 가지로 뻗어나감
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(board, loc): 
    # board에서 현재 위치가 loc일 때 움직일 수 있는 지 판단
    x, y = loc
    for i in range(4): # 한 경우라도 움직일 수 있으면 True
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<= nx < len(board)) and (0<= ny <len(board[0])) and (board[nx][ny] == 1):
            return True
    return False
    
    
def search(board, aloc, bloc, step): # step은 0부터 시작. 0-A, 1-B, 2-A...
    if step % 2 == 0: # A의 차례
        x, y = aloc
    else: # B 차례
        x, y = bloc
        
    # 지는 경우: 1. 상하좌우가 다 0인 경우 2. 두 플레이어가 같이 있는 경우
    if not check(board, [x,y]):
        return (False, 0)  # 다음 번까지 가지 않고 끝남
    if aloc == bloc:
        return (True, 1) # 다음 번에 끝이 남
    
    nboard = deepcopy(board) 
    nboard[x][y] = 0 # 플레이어 현재 위치 방문
    flag = False # 내가 우승할 수 있는 지 여부
    winner, loser = 0, 9999999
    
    for i in range(4): # 한 경우라도 움직일 수 있으면 True
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<= nx < len(board)) and (0<=ny < len(board[0])) and (nboard[nx][ny] == 1):
            if step % 2 == 0: # 이제 B의 차례
                result = search(nboard, [nx, ny], bloc, step+1)
            else: # 이제 A의 차례
                result = search(nboard, aloc, [nx, ny], step+1)
            
            if result[0]: # 상대가 이겼다 (나는 졌다)
                #flag = False
                winner = max(winner, result[1])
            else: # 상대가 졌다 (나는 이겼다)
                flag = True
                loser = min(loser, result[1])
    
    if flag: # 내가 이길 수 있으면
        return (flag, loser+1)
    else:
        return (flag, winner+1)
    
def solution(board, aloc, bloc):
    '''
    - 발판이 있는 곳만 캐릭터가 서 있을 수 있음. 캐릭터가 밟고 나면 발판이 사라짐.
    - 플레이어 A,B는 상,하,좌,우 인접한 네 칸 중 발판이 있는 곳으로 움직임
    - A가 먼저 시작
    패배 기준: (1) 네 칸 모두 발판이 없거나 보드 밖. (2) 같은 발판에 있다가 한 명이 움직임
    
    <input>
    board: 게임 보드의 초기 상태를 나타내는 2차원 배열
    aloc: A의 초기 위치, bloc: B의 초기 위치
    
    <output>
    두 캐릭터가 움직인 횟수의 합
    
    알고리즘: DFS, 완전탐색
    idea: minimax
    이기는 플레이어는 최소의 움직임으로, 지는 플레이어는 최대의 움직임으로
    '''
    return search(board, aloc, bloc, 0)[1] # search는 (True/False, cnt) 를 반환하는 함수

# 참고: https://tiktaek.tistory.com/88, https://velog.io/@mrbartrns/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%82%AC%EB%9D%BC%EC%A7%80%EB%8A%94-%EB%B0%9C%ED%8C%90-python