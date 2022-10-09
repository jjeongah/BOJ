# 아이디어는 빨리 떠올랐으나 구현에서 시간 소요
def solution(n,a,b):
    # n명의 참가자. A번과 B번이 몇 번째 라운드에서 만날까?
    # 이긴 사람(N번)은 다음 라운드에 N/2번 
    cnt = 1 #몇번째에서 차이가 1만큼 나는지. 단, 작은 값은 홀수, 큰 값은 짝수여야함
    while a>0 and b>0:
        if abs(a-b)==1:
            if max(a,b)%2== 0 and min(a,b)%2!=0:
                break
        cnt += 1
        if a%2==0:
            a/=2
        else:
            a = (a+1)/2
        if b%2==0:
            b/=2
        else:
            b = (b+1)/2
    return cnt