'''
뭉치 내에서는 순서대로 다 쓰면서 넘어가야함
card1, card2 겹치는 단어 없고 goal은 card1,2 내 문자로 구성됨
* 단어 간 순서가 동일한가?

for i in range(len(cards1)-1):
        for j in range(i+1,len(cards1)):
            if goal.index(cards1[i]) > goal.index(cards1[j]):
                return 'No'
    for i in range(len(cards2)-1):
        for j in range(i+1,len(cards2)):
            if goal.index(cards2[i]) > goal.index(cards2[j]):
                return 'No'
    return 'Yes'
'''
def solution(cards1, cards2, goal):
    # goal의 단어를 기준으로 idx 증가하면서 안 뽑고 넘어가는 지 확인
    # goal의 단어는 반드시 cards1이나 2에 있어야 한다
    idx1, idx2 = 0, 0
    for item in goal:
        if idx1 < len(cards1) and cards1[idx1] == item:
            idx1+=1
        elif idx2 < len(cards2) and cards2[idx2] == item:
            idx2+=1
        else:
            return 'No'
    return 'Yes'