'''
축구를 하기 위해 모인 짝수 N명 - 스타 / 링크 팀으로 나눈다
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다
팀의 능력치는 모든 쌍의 능력치의 합이다 (a,b가 속하면 Sab + Sba)

return : 스타팀과 링크팀 능력치 차이의 최솟값
idea: 그리디? DP?
대각선을 기준으로 합을 구하는
'''
from itertools import combinations
import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

def calculate(arr, a, b):
    return arr[a][b] + arr[b][a]

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
#print(arr)
#print(list(combinations(range(N), N//2)))
combi = list(combinations(range(N), N//2))
#print(len(combi))
diff = float('inf')

for start in combi[:len(combi)//2]:
    members = [x for x in range(N)]
    link = [x for x in members if x not in start]
    #print(start, link)
    
    s_score = 0
    l_score = 0
    for a,b in list(combinations(start, 2)):
        s_score += calculate(arr, a, b)
    for a,b in list(combinations(link, 2)):
        l_score += calculate(arr, a, b)
    #print(s_score, l_score)
    diff = min(abs(s_score - l_score), diff)

print(diff)
