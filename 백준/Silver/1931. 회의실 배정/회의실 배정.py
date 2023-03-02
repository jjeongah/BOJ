'''
한 개의 회의실을 N개의 회의에 대해 사용
겹치기 않게 하면서 사용할 수 있는 회의의 최대 개수
하나가 끝남과 동시에 시작할 수 있음

진짜 아이디어조차 떠오르지 않는다
앞에서부터 선택하면서 모든 경우의 수 고려하는 것 아님

정렬: 회의 시간 기준 아님
1. 끝나는 시간 오름차순
2. 회의 끝나는 시작이 같을 경우 더 늦게 시작하는 순서(시작 시간 오름차순)
'''
#import sys
#sys.stdin = open('./input.txt', 'r')

N = int(input())
arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])
#print(arr)
arr = sorted(arr, key = lambda x: (x[1], x[0]))
start, end = arr[0][0], arr[0][1]
cnt = 1
for i in range(1, len(arr)):
    if arr[i][0] >= end:
        cnt += 1
        start, end = arr[i][0], arr[i][1]
print(cnt)