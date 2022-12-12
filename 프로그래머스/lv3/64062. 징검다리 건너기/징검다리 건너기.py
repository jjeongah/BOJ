'''
이진탐색
'''

def solution(stones, k):
    answer = 0
    left, right = min(stones), max(stones) 
    cnt = 0 # 연속된 0의 개수
    
    while left <= right:
        cnt = 0
        mid = (left + right)//2
        for s in stones: # mid명이 건널 수 있는 지를 확인
            if s-mid <= 0: # 0이 연속적으로 나오는 경우
                cnt += 1
            else:
                cnt = 0 # 0이 연속적으로 안 나오면 초기화
            if cnt >= k: # 더 이상 건널 수 없는 경우
                break
        if cnt < k: # 더 많이 건널 수 있음
            #answer = mid
            left = mid + 1
        else: # 덜 건너야 함
            answer = mid
            right = mid -1
            
    return answer
        