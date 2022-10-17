def convert(i, n):
    temp = "0123456789ABCDEF"
    q, r = divmod(i, n) # i//n, i%n
    if q == 0:
        return temp[r]
    else:
        return convert(q, n) + temp[r]
    
def solution(n, t, m, p):
    # n진법, 미리 구할 숫자의 개수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    # 튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 출력
    
    # 10진수를 n진수로 변환할 값을 "t*m개" 나열하기  (10진수가 아니라면 t*m보다 적게 필요할 수 있음)  
    # p-1번째, (p-1)+m번째, (p-1)+2m번째 ... 값을 answer에 concat
    
    numbers = ''
    for i in range(t*m): # 십진수 i를 n진수로 변환
        numbers += convert(i,n)
    
    tube = ''
    idx = p-1
    while len(tube) < t:
        tube += numbers[idx]
        idx += m
    return tube