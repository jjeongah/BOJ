'''
    cnt = 0 #롤케이크를 공평하게 자르는 방법의 수
    for i in range(len(topping)):
        if len(set(topping[:i])) == len(set(topping[i:])):
            cnt += 1
    return cnt
'''
from collections import Counter
def solution(topping):
    '''
    동일한 가짓수의 토핑이 올라가게 (종류의 개수가 중요)
    '''
    type = Counter(topping)
    #print(type)
    cnt = 0 #롤케이크를 공평하게 자르는 방법의 수
    CS = set() # Cheol Su
    # 하나를 뽑으면 전체 토핑에서 하나가 빠진다고 생각
    for i in topping:
        type[i] -= 1
        if type[i] == 0:
            type.pop(i)
        CS.add(i)
        if len(type) == len(CS):
            cnt += 1
        #print(len(type)) #Set은 개수가 0이더라도 value가 있으면 count함
        #print(type)
    return cnt
    