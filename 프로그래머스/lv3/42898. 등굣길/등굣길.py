def solution(m, n, puddles):
    '''
    (1,1)에서부터 (m,n)까지 paddles를 피해서 가는 방법의 수 
    * 1,000,000,007로 나눈 나머지 => 왜 나눔?
    
    * 행과 열이 반대이다
    (1,1) (2,1) ... (m,1)
    (1,2)
    ...
    (1,n)           (m,n)
    
    * 전형적인 2차원 dp문제
    dp[i][j] : (i,j)까지 갈 수 있는 경우의 수
    dp[i][j] = dp[i-1][j] + dp[i][j-1] (왼, 오 두 방향만 갈 수 있으므로)
    '''
    puddles = [[b-1,a-1] for [a,b] in puddles] 
    dp = [[0]*(m) for i in range(n)] # dp 초기화
    dp[0][0] = 1 # 집(시작)의 위치
    
    for i in range(n):
        for j in range(m):
            if n == 0 and m == 0:
                continue
            if [i,j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] += (dp[i-1][j] + dp[i][j-1])
    print(dp)             
    return dp[n-1][m-1]  % 1000000007