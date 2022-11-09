def solution(enroll, referral, seller, amount):
    '''
    <input>
    enroll: 판매원 이름 (민호 제외)
    referral: 각 판매원을 데리고 온 판매원 이름 (-는 민호로)
    seller: 각 판매량 당 판매원 이름
    amount: 각 판매원의 이익금
    
    <output>
    (민호 제외) 각 판매원의 합산한 이익금을 list로 반환
    
    <문제 설명>
    자기의 이익금의 90%를 가짐
    10%는 추천인에게 (1원 미만이라면 자신이 다 가짐)
    
    <idea> 
    판매원- 추천인 관계를 어떤 식으로 파악할 것인가 
    => 1. zip(seller, amount)로 각 판매원 별 이익금 정리 
    '''
    answer = [0 for _ in range(len(enroll))]
    dict = {}
    for num, e in enumerate(enroll):
        dict[e] = num
    #print(dict) #{'john': 0, 'mary': 1, 'edward': 2, 'sam': 3, 'emily': 4, 'jaimie': 5, 'tod': 6, 'young': 7}
    for s, a in zip(seller, amount):
        money = a* 100
        
        # 민호까지 돈이 들어오거나 줄 돈이 없으면 종료
        while True:
            if s =='-' or money <= 0:
                break
            idx = dict[s] # 지금 계산하는 seller의 enroll에서의 idx
            answer[idx] += money - money//10
            money //= 10
            s = referral[idx] # 지금 계산하는 seller의 추천인
    return answer