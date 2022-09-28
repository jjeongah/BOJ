import sys
input = sys.stdin.readline

N = int(input())
dp = [x for x in range(N+1)] # dp[x]의 최대(최악값은) 1을 x개만큼 했을 때

for i in range(1, N+1): # dp[N]까지 값을 찾는다
    for j in range(1, i): # dp[1]일때 1*1, dp[2]일때 1*1, 2*2(break),... dp[10]일때 1*1, .., 3*3, 4*4(break)
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] +1: # 더 작은 dp[i-j*j]의 값을 발견하면
            dp[i] = dp[i-j*j] + 1
print(dp[N])
