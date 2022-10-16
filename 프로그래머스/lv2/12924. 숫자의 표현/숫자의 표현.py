def solution(n):
    # 자연수 n을 연속된 자연수로 표현하는 방법의 수 
    # DP 등의 방식으로 못 푼다 => 완전 탐색
    
    cnt = 1 # 자기 자신
    for i in range(1, n):
        sum = 0
        for j in range(i, n):
            sum += j
            if sum == n:
                cnt += 1
            elif sum > n:
                break 
    return cnt