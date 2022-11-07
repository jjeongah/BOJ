from collections import deque

def solution(q1, q2):
    '''
    q1, q2 원소의 합이 동일하게
    pop, insert를 묶어서 한 번의 작업으로 친다
    총 작업을 몇 번 수행했는 지 return
    
    idea: 
    어떤 큐에서 몇 개의 원소를 뺴야하는가?
    => 
    1. greedy (deque 사용)
    처음 주어진 q1의 합을 L, q2의 합을 R이라고 할 때,
    L > R이라면 q1에서 q2로, L < R이라면 q2에서 q1으로
    2. 투 포인터 
    q1, q2를 이어서 하나의 배열로 생각하고 
    (L+R)/2에 있는 포인터를 이동
    '''
    q1, q2 = deque(q1), deque(q2)
    L, R = sum(q1), sum(q2)
    
    # 어떤 방법으로도 L, R 같아지지 않는 경우
    if (L+R)% 2 != 0:
        return -1
    
    # while문으로 하면 [1,1],[1,2]와 같은 케이스에서 무한 루프
    # for문으로 횟수를 지정해야 한느디 len(q1)*2로 하면 1번 케이스 안됨
    for cnt in range(len(q1)*3):
        if L == R:
            return cnt
        elif L > R:
            tmp = q1.popleft()
            q2.append(tmp)
            R += tmp
            L -= tmp
        elif L < R:
            tmp = q2.popleft()
            q1.append(tmp)
            R -= tmp
            L += tmp
    return -1 # [1,1], [1,5]와 같은 케이스

# https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/