# k층 n호에는 몇 명이 사는가
# DP 문제
import sys
input = sys.stdin.readline

# bottom up 방식으로 미리 arr 구해두기
arr=[[0 for j in range(15)] for i in range(15)]
for i in range(15):
    arr[0][i] = i
for i in range(1,15):
    for j in range(1, 15):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]
        
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(arr[k][n]) # arr[k][n] : k층 n호

