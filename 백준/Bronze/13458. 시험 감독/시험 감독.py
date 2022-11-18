'''
N개의 시험장 (i번째 시험장에 있는 응시자 수는 Ai명)
총감독관이 B명 감시, 부감독관이 C명 감시
시험장에 총감독관은 반드시 1명, 각 시험장마다 감시관이 있어야 함

출력: 필요한 감독관의 최솟값
'''

import math
#import sys
#sys.stdin = open('./input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
B, C = map(int, input().split())
# print(N, arr, B, C)
cnt = 0 # 감독관의 수

for num in numbers:
    if num <= B:
        cnt +=1
    else:
        cnt += math.ceil((num - B)/C) + 1
print(cnt)