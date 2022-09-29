# 소수 판별 시 주의: 1은 소수가 아니다
# x를 2부터 int(x**0.5)+1 까지 나눠보면서 나눠 떨어지면 소수가 아님

import sys
input = sys.stdin.readline

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) +1):
        if x%i == 0:
            return False
    return True

N = int(input())
arr = list(map(int, input().split()))
answer = 0
for i in arr:
    if isPrime(i) == True:
        answer +=1

print(answer)