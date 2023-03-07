'''
수포자 세 명 중 누가 제일 점수 높냐
여러 명이 동점이면 오름차순 return

반복 패턴 개수가 다른 거 어떻게?
'''
def solution(answers):
    a = [1,2,3,4,5] #5
    b = [2,1,2,3,2,4,2,5] #8
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10
    tmp = []
    score_a, score_b, score_c = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            score_a += 1 
        if answers[i] == b[i%8]:
            score_b += 1
        if answers[i] == c[i%10]:
            score_c += 1
    max_score = max(score_a, score_b, score_c)
    if score_a  == max_score:
        tmp.append(1)
    if score_b  == max_score:
        tmp.append(2)
    if score_c  == max_score:
        tmp.append(3)
    return tmp