'''
우승자는 숫자파 두개를 정해진 횟수만큼 위치 교환한다
같은 위치 두 번해서 원래대로 돌아오기 가능

return: 교환후 최대값

<idea>
1. 모든 경우의 수를 전부 비교하면(완전탐색) 시간 초과
=> 백트래킹

2. 자릿수 고려
- 가장 큰 값과 가장 작은 값을 우선 바꾸는 게 아님 => 자릿수를 비교해서 맨 앞자리에 큰 값이 오게
- 앞쪽 숫자가 뒤쪽 숫자보다 작으면 그 둘을 바꾼다 -> 32888은 88328이 아니라 88832임

3. 최대값에 도달할 수 있는 경우
**최대값을 만드는 동전의 최소 교환횟수**를 넘으면 마지막 두 숫자만 바꿔가면서 횟수를 채울 것임
'''
def dfs(index, count):
    global result # 교환 후 받을 수 있는 최대 금액
    if count == cnt: # 1. 종료조건
        result = max(int(''.join(num)), result)
        return
    
    # 2. 앞쪽 숫자가 뒤쪽 숫자보다 작으면 그 둘을 바꾼다
    for now in range(index, len(num)):
        for big in range(now+1, len(num)):
            if num[now] <= num[big]: # **** <로 하면 77732 1과 같은 테케 실패
                num[now], num[big] = num[big], num[now]
                dfs(now, count+1)
                num[now], num[big] = num[big], num[now] # 원상복귀 (다른 경우를 확인하기 위해)

    # 3. ** 이미 내림차순으로 정렬됐는데(뒤쪽 큰 값을 찾으며 내림차순 정렬을 완료했는데) 교환 횟수를 소모하지 못한 경우
    # 홀수면 맨 뒤 두 개 교환, 짝수면 그대로 반환
    if result == 0 and count < cnt:
        if (cnt - count)%2 == 1: # 홀수
            num[-1], num[-2] = num[-2], num[-1]
        dfs(index, cnt)

N = int(input())
for i in range(1,N+1):
    num, cnt = input().split() # num은 list로 만들어야 하니까 int로 바꾸면 안됨
    num = list(num)
    cnt = int(cnt)
    result = 0
    dfs(0, 0) #(index, count) count가 cnt와 같아질 때까지 num 리스트의 index를 증가하면서 체크
    print("#{} {}".format(i, result))