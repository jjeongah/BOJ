'''
구현 문제

arr = [x for x in zip(range(1, len(cards)+1), cards)]
처음에 [(1, 8), (2, 6), (3, 3), (4, 7), (5, 2), (6, 5), (7, 1), (8, 4)] 묶어주려고 했음
그러나 idx+1이 곧 박스의 넘버이므로 할 필요 X
''' 


def solution(cards):
    # 1~100 숫자카드 중 n개를 뽑고 n개의 상자 준비
    # 1번 상자 열기 -> [1번 상자 안의 카드 숫자] 열기 -> .... "1번 상자 그룹"
    # 1번 상자 그룹만 있으면 0점, 1번 상자그룹 상자 수 x 2번 상자 그룹 상자 수 
    # 최고 점수 return
    answer = 0
    for x in cards: #어떤 카드가 있는 상자부터 열기 시작할 지
        open = [False] * len(cards)
        cnt_1 = 0 # 첫번째 그룹 박스 수
        idx = x # 첫 상자 안에 있는 카드
        while True: # 여는 건 open list 원소값만 바꿔주면 됨
            if open[idx-1] == False: # !! 주의: 번호는 1~len(cards)인데 cards와 open의 idx는 0~len(cards)-1
                open[idx-1] = True  
                cnt_1 += 1
                idx = cards[idx-1]
            else: 
                break
            
        arr = [] # 1번 그룹에 속하지 않는 카드들
        for i in range(len(cards)): # idx는 0~len(cards)-1
            if open[i] == False:
                arr.append(cards[i])
        if not arr:  # 1번 상자 그룹으로 끝날 경우
            break # !! 주의: 냅다 0 return해주면 안됨 / 이유: 다른 카드부터 열기 시작했을 떄 그룹 두 개일 수도
        
        # 2번 그룹 만들기
        cnt_2 = 0        
        for x in arr: # 다음 카드 어떤 것부터 열어볼 지 전부 비교
            tmp = 0  # !! 주의: cnt_2도 어떤 카드부터 열지에 따라 다르니까 값 바로 갱신하지 말고 max로 전 경우 비교
            idx = x
            while True:
                if open[idx-1] == False:
                    open[idx-1] = True
                    tmp += 1
                    idx = cards[idx-1]
                else:
                    cnt_2 = max(cnt_2, tmp) 
                    break
        answer = max(answer,cnt_1*cnt_2)
    return answer