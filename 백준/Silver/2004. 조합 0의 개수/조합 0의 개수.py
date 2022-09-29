# 틀린 접근법:[1] itertools combinations는 경우의 수를 print해주므로 사용 X
# [2] 값을 구하고 0 세기: math.factorial을 사용시 시간 초과
# => 올바른 풀이: 0의 개수는 2와 5의 승수 중 최소값

import sys
import math
input = sys.stdin.readline

def cnt_num(x, num): 
    # x!(factorial)의 num(2또는 5)가 몇 번 곱해져 있는가
    # => x//2 + x//4 + x//16 +....
    cnt = 0
    while x > 0:
        cnt += x//num
        x = x//num 
        # x= x-1이 아닌 이유는 x=5, num=2일 때 
        # 5//2 + 4//2 + 3//2 +...가 아니라 5!//2 + 5!//4+ .. 이기 때문
    return cnt

n, m = map(int, input().split())
# [1] n!, m!, (n-m)!의 2, 5의 개수를 구하고
# [2] 개수 간 빼기 
answer = min(cnt_num(n,2)-cnt_num(m,2)-cnt_num(n-m,2), cnt_num(n,5)-cnt_num(m,5)-cnt_num(n-m,5))

print(answer)