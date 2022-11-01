''' # **** 효율성 테스트 실패 ****
def solution(n, works):
    야근 피로도: 야근 시점에서부터 남은 일의 작업량을 제곱하여 더한 값
    한 시간 동안 작업량 1만큼 처리
    
    input: 
    퇴근까지 남은 N 시간, 각 일에 대한 작업량 works
    
    output:
    야근 피로도를 최소화한 값 return
    
    idea: 
    sort를 매번 해주면서 가장 큰 값에 -1
    if n >= sum(works): # 남는 작업량이 없을 때
        return 0
    
    works.sort(reverse = True)
    for _ in range(n):
        works[0] -= 1
        works.sort(reverse = True)
    
    print(works)
    return sum([w**2 for w in works])
'''

import heapq
def solution(n, works):
    '''
    heapq는 heappop으로 최솟값만 pop하니까
    -를 붙이면 됨
    
    예제 1. [-4, -3, -3] => [-3, -3, -3] => [-2, -3, -3] => [-2,-2,-3] => [-2,-2,-2]
    '''
    if n >= sum(works): # 남는 작업량이 없을 때
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    cnt = 0
    while True:
        if cnt == n:
            break
        max = heapq.heappop(works)
        heapq.heappush(works, max+1) 
        cnt += 1
    print(works)
    
    return sum([w**2 for w in works])