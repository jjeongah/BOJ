''' # 시간 초과
from itertools import combinations_with_replacement
def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    multi = -1
    for arr in combinations_with_replacement(list(range(1, s)), n):
        if sum(arr) == s:
            temp = 1
            for i in arr:
                temp *= i
            if multi <= temp:
                multi = temp
                answer = arr
    return answer
'''
def solution(n, s):
    '''
    원소의 개수 n (각 원소는 자연수)
    원소들의 합 s
    
    각 원소의 합이 s이면서도 원소의 곱이 최대인 집합을 return(오름차순 정렬)
    
    idea: 언제 곱이 최대? => 원소 간 값 차이가 적을 때 => s//n
    s%n이 0이 아니라면? => 맨 뒷자리부터 1씩 더해줌
    ex. n = 4, s = 9 -> [2,2,2,2] -> [2,2,2,3]
    '''
    answer = []
    if n > s:
        return [-1]
    
    for _ in range(n):
        answer.append(s//n)
    
    idx = -1
    for _ in range(s%n):
        answer[idx] += 1
        idx -= 1
    
    return answer
