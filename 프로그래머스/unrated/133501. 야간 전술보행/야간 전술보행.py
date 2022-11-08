def solution(distance, scope, times):
    n = len(scope)
    # scope의 원소들을 정렬한 뒤 순번 append
    for i in range(n) :
        scope[i].sort()
        scope[i].append(i)
    scope.sort() # scope 정렬
    
    # 순번 : time으로 하는 딕셔너리 생성
    times_dict = {i : times[i] for i in range(n)}
    
    # 해당 경비병 근무 시간에 걸리면 바로 return 
    for i in range(n) :
        start, end, key = scope[i]
        work, rest = times_dict[key]
        
        for num in range(start, end + 1) :
            if (num-1) % (work + rest) <= work-1 :
                return num
    
    # 안 걸리면 최대 거리 return
    return distance