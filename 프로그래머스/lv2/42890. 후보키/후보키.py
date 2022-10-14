# python의 자료형을 적재적소에 쓰는 게 어려웠던 문제

from itertools import combinations 
def solution(relation):
    '''
        2차원 배열 relation [속성][튜플]
        후보 키의 개수를 return
        
        idea: combinations으로 전체 경우의 수 구하고 아래 기준으로 거른다
              1. 유일성 -> set에 넣었을 때랑 개수가 동일
              2. 최소성 -> 부분집합이 아니어야 함
        issue: 두 개 이상의 속성을 조합했을 때 경우의 수 어떻게 구할까
    '''
    answer = 0 # 후보키의 개수
    row, col = len(relation), len(relation[0]) #2차원 배열의 행, 렬 구하기
    candidates = [] # 원소값이 아닌 키의 idx 경우의 수
    for i in range(1, col +1): # col+1 개의 키 중 1개, 2개, ... col+1개를 뽑는 경우
        candidates.extend(combinations(range(col), i))
        # append는 리스트 끝에 1개를 그대로 넣음/ extend는 같은 배열로 추가
    #print(candidates)
    
    # idx candiated로 실제 값들 비교
    unique_can = []
    for cand in candidates:
        all_can = [tuple(row[col] for col in cand) for row in relation]
        # tuple의 역할 모르겠음
        '''
        for row in relation: # 하나의 row
            for col in cand: 
                all_can.append(row[col])
        '''
        if len(all_can) == len(set(all_can)): # 1. 유일성
            flag = True
            for x in unique_can: # 2. 최소성
                if set(x).issubset(set(cand)):
                    flag = False
            if flag: 
                unique_can.append(cand)
    print(unique_can)
    return len(unique_can)