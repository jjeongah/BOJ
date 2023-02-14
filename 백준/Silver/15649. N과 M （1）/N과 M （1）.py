'''
1~N까지 자연수 중에서 중복 없이 M개를 고른 수열
N C M
'''
#import sys
#sys.stdin = open('./input.txt', 'r')
#input = sys.stdin.readline

def dfs():
    if len(temp) == M:
        print(*temp)
        return 
    for i in range(N): # arr의 i번째 인덱스 값 검사
        if arr[i] not in temp:
            temp.append(arr[i])
            dfs()
            temp.pop()

N, M = map(int,input().split())
arr = [x for x in range(1, N+1)]
temp = [] # 나올 수 있는 combination을 담는 list
dfs()