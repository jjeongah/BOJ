import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin_type = []
for _ in range(N):
    coin_type.append(int(input()))
answer = 0

# coin_type에서 큰 값부터 K값과 비교하며
# 개수 = K / coin_type[i], 남은 값은 K % coin_type[i]
i = len(coin_type)-1
while K > 0 and i >= 0:
    if coin_type[i] <= K:
        answer += K // coin_type[i]
        K = K % coin_type[i]
    i -=1
print(answer)