from collections import deque

def bfs(n, info):    
    answer = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
                # 둘 다 0점이면 둘 다 점수 못 가져가므로 lion == 55- apeach 아님 
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap: #최대 점수차 안넘으면 다음거나 검사
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                answer.append(arrow)  # 최대점수차를 내는 화살상황 저장
                #??? 왜 먼저 하면 안됨?
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp)) #focus 아무값이나 넣어줘도 됨 -> 이미 끝난 상황
        
        else:  # 화살 쏘기
            tmp = arrow.copy() #왜 tmp = arrow는 안됨? 어차피 얕은 복사 아님?
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return answer

def solution(n, info):
    answer = bfs(n, info)
    
    if answer == []:
        return [-1]
    return answer[-1]
