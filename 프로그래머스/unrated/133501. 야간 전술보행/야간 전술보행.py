'''
Try 1 : 구현하다가 이렇게 다 찾을 필요없음 깨달음

<idea>
1. 경비병 별 감시/휴식을 미리 계산 =>
   휴식 시간 == [work+ (work+rest)*N, work+ (work+rest)* (N+1)]
   시간 % (work+rest) 가 1~work 사이의 값이면 근무, 아니면 휴식중임
2. 감시 구간에 해당 경비병이 감시(1) 하는지 휴식(0)하는 지를 담은 list(size가 distance) 만들기

def solution(distance, scope, times):
    answer = 0
    
    arr = [0]*(distance+1) # 경비병 감시/휴식 정보 합산
    N = len(times) # 경비병의 수 
    info = [0]*(distance+1) # 한 명의 경비병 감시/휴식 정보 합산
    
    for i in range(N):
        info = [0]*(distance+1)
        
        # 1. 각 경비원의 감시/휴식 정보 불러오기
        work, rest = times[i]
        for j in range(N):
            if 0 < j % (work+rest) <= work:
                info[j] = 1
        
        # 2. 필요한 부분만 합산해주기
        start, end = sorted(scope[i]) # ** 정렬
        for k in range(start, end+1):
            arr[k] = info[j]
        
    return answer
'''

'''
Try 2 : scope도 시간 순으로 정렬한 게 아니므로 모든 경비원을 다 체크하지 않고 끝남

def solution(distance, scope, times):
    answer = 0
    info = [] # 경비병 감시/휴식 정보 append 해냐감
    N = len(times) # 경비병의 수 

    for i in range(N): # 경비원을 하나씩 불러옴
        start, end = sorted(scope[i]) # ** 조건: scope[i]는 정렬되어 있지 않을 수 있습니다
        
        # 각 경비원의 감시/휴식 정보 불러옴과 동시에 근무중이면 return
        work, rest = times[i]
        for j in range(start, end+1):
            if 0 < j % (work+rest) <= work:
                return j
            
    return distance
'''

def solution(distance, scope, times):
    '''
    <input>
    distance: 화랑이의 현재 위치와 적군 기지 사이의 거리
    scope: 각 경비병의 감시 구간 [시작 idx, 끝 idx]
    times: 각 경비병의 휴식 시간 [work, rest sec]
    
    <output>
    화랑이가 경비병을 피해 이동할 수 있는 최대거리
    '''
    answer = 0
    info = [] # 경비병 감시/휴식 정보 append 해냐감
    N = len(times) # 경비병의 수 
    stop = [distance] # 걸리는 경우 - 안 걸리면 distance 반환
    stopped = False # 걸렸는 지 여부
    
    for i in range(N): # 경비원을 하나씩 불러옴
        start, end = sorted(scope[i]) # ** 조건: scope[i]는 정렬되어 있지 않을 수 있습니다
        
        # 각 경비원의 감시/휴식 정보 불러옴과 동시에 근무중이면 return
        work, rest = times[i]
        for j in range(start, end+1):
            if 0 < j % (work+rest) <= work:
                stop.append(j)
                
    return sorted(stop)[0]
                