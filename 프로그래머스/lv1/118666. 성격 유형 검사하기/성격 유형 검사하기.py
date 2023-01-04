'''
더 높은 점수를 받은 게 성격 유형(지표)
점수가 같으면 사전 순으로 빠른 거

survey: 질문이 판단하는 지표 (XY. 비동의시 X, 동의시 Y)
choices: 선택
[1- 매우 비동의(+3), 2-비동의(+2), 3-약간 비동의(+1), 4, 5-약간 동의(+1), 6-동의(+2), 7-매우 동의(+3)]
검사자의 결과를 지표 번호 순서대로 입력
'''
def solution(survey, choices):
    answer = ''
    type = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = {x:0 for x in type}
    #print(score)
    
    for i in range(len(survey)):
        X, Y = survey[i][0], survey[i][1]
        #print(X, Y)
        if choices[i] < 4: # 비동의 (X)
            score[X] += 4-choices[i]
        else: # 동의(Y)
            score[Y] += choices[i]-4 
            
    if score['R'] < score['T']:
        answer += 'T'
    else:
        answer +='R'
    if score['C'] < score['F']:
        answer += 'F'
    else:
        answer +='C'
    if score['J'] < score['M']:
        answer +='M'
    else:
        answer +='J'
    if score['A'] < score['N']:
        answer +='N'
    else:
        answer +='A'
    return answer