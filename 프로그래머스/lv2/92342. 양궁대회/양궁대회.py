'''
10점~0점
각 점수마다 많이 맞힌 사람이 점수를 가져감 (동점이면 어피치, 둘 다 0점이면 아무도 못 가져감)
어피치가 n발을 쐈을 때 라이언이 최대 차로 이기는 방법은?

높은 점수에 몰거나 낮은 점수 여러 개에 배팅 => 어떻게 찾을까?
중복조합(0~10까지를 n개 고른다)/BFS
'''
from collections import deque

def bfs(n, info):    
    answer = [-1]
    q = deque()
    q.append([0, [0]*11])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0): # 둘 다 0점이면 안됨
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap: # = 들어가면 안됨 
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                answer= arrow # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((10, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return answer

def solution(n, info):
    answer = bfs(n, info)
    return answer