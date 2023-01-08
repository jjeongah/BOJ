'''
N개의 수열, N-1개의 연산자
%는 몫을 구함. 앞에서부터 차례로
'''
#import sys
#sys.stdin = open('./input.txt', 'r')
#input = sys.stdin.readline

N = int(input()) # 수의 개수
num = list(map(int, input().split())) # A1,.., An (0은 없음)
oper = list(map(int, input().split())) # 차례대로 +, -, x, % 개수
# oper 경우의 수 : DFS 백트래킹
# idea: 수와 사칙연산을 어떻게 계산?
maximum = -float('inf')
minimum = float('inf')

def dfs(cnt, total, plus, minus, multiply, divide):
    global maximum, minimum # global 선언 안하면 -1, inf 출력
    if cnt == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return 
    if plus != 0:
        dfs(cnt+1, total + num[cnt], plus-1, minus, multiply, divide)
    if minus != 0:
        dfs(cnt+1, total - num[cnt], plus, minus-1, multiply, divide)
    if multiply != 0:
        dfs(cnt+1, total * num[cnt], plus, minus, multiply-1, divide)
    if divide != 0:
        dfs(cnt+1, int(total / num[cnt]), plus, minus, multiply, divide-1)

dfs(1, num[0], oper[0], oper[1], oper[2], oper[3]) # 다음 num을 표시하기 위해서는 cnt 사용
print(maximum)
print(minimum)
