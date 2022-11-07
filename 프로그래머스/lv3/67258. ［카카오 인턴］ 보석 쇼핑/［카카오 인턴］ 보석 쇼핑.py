''' # 테케 11~15 시간 초과
# 보통 효율성을 테스트하는 문제는 O(n)으로 해결 가능하다
# 완전 탐색은 O(N^2)
# 리스트 슬라이싱은 객체 k 개를 조회해야해서 O(k^2)

def solution(gems):
    species = len(set(gems))
    answer = []
    temp = 9999
    for i in range(0, len(gems)- species+1):
        for j in range(min(i+species-1, i+1), len(gems)):
            #print(i+1, j+1, set(gems[i:j]), set(gems))
            if len(set(gems[i:j+1])) == species:
                if j-i < temp:
                    answer = [i+1, j+1]
                    temp = j-i
    return answer    
'''

def solution(gems):
    '''
    진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간
    
    <input>
    gems: 보석 배열
    
    <output>
    [시작 idx, 마지막 idx]
    
    <idea>
    1. dict 사용 / dic[보석 이름] = 빈도수
    2. 투 포인터(l,r) : 
        l,r은 0에서 시작해서 끝점이 증가하면서 구간을 느려가고, 시작점이 증가하면서 구간을 줄여나간다
       - 포인터가 범위 벗어나면 종료
       - map 안의 보석 종류 개수 확인
       - 전체 보석 종류와 일치하면 l 증가
       - 보석 종류가 부족하면 r 증가
    '''
    species = len(set(gems))
    N = len(gems)
    answer = [0, N-1]
    dic = {} # 구간에 포함된 보석
    dic[gems[0]] = 1
    l, r = 0, 0

    while 0<= l< N and 0<= r < N:
        if len(dic) < species: # 1. 보석 부족 => 끝점 이동
            r += 1 # 시작하자마자 r을 옮겨서 gems[0]은 추가 못함
            if r == N:
                break
            dic[gems[r]] = dic.get(gems[r], 0) + 1 
            # get: dict에 gems[r]이 있으면 gems[r] 반환, 없으면 0 반환
            
        else: #if len(dic) == species / 2. 전체 보석 종류와 일치 - 길이 비교
            if r-l < answer[1]- answer[0]: # 1-1. 최소 길이면 갱신
                answer = [l,r]
            # 1-2. 최소 길이 아니면 l 이동
            if dic[gems[l]] == 1: # 원소 삭제할 때 1개 존재하는 거 주의
                del dic[gems[l]]
            else:
                dic[gems[l]] -= 1
            l += 1
        
        
    return [answer[0]+1, answer[1]+1]

# https://dev-note-97.tistory.com/70
            
        