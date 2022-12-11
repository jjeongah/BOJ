'''
길이가 같은 두 큐
작업 1회 : 한 번 pop하고 insert함
'''
from collections import deque

def solution(q1, q2):
    q1, q2 = deque(q1), deque(q2)
    L, R = sum(q1), sum(q2)
    answer = 0
    cnt = len(q1)*3

    while answer <= cnt:
        if L == R:
            return answer
        elif L < R: #q2에서 q1으로 옮기기
            tmp = q2.popleft()
            q1.append(tmp)
            R -= tmp
            L += tmp
            answer += 1
        elif L > R:
            tmp = q1.popleft()
            q2.append(tmp)
            R += tmp
            L -= tmp
            answer += 1
    return -1