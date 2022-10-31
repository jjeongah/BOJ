from collections import Counter

def solution(str1, str2):
    '''
    자카드 유사도 J(A, B): 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
    (A,B가 공집합인 경우, 1 / 중복 허용하는 다중집합에도 적용)
    
    입력: 문자열을 두 글자씩 sliding하며 끊어서 원소로 (대소문자 상관 X. 영어여야함)
    출력: 자카드 유사도(0~1 사이 실수값) * 65536 의 정수부분만
    
    idea: 
    - set은 중복 제거해서 사용하면 안됨
    - Counter을 사용하려면 	[['f', 'r'], ['a', 'n'], ['c', 'e']]가 아니라 
      ['fr', 'an', 'ce']의 형태여야함
    '''
    # 1. 다중집합 만들기
    s1 = list(str1)
    s1 = [i.lower() for i in s1]
    arr1 = []
    for i in range(len(s1)-1):
        if s1[i].isalpha() and s1[i+1].isalpha():
            arr1.append(''.join(s1[i]+s1[i+1]))
    
    s2 = list(str2)
    s2 = [i.lower() for i in s2]
    arr2 = []
    for i in range(len(s2)-1):
        if s2[i].isalpha() and s2[i+1].isalpha():
            arr2.append(''.join(s2[i]+s2[i+1]))
    
    print(arr1)
    print(arr2)
    
    # 2. 교집합 개수 구하기
    # ** 각 원소의 최대, 최댓값
    tmp1 = Counter(arr1)
    tmp2 = Counter(arr2)
    print(tmp1)
    print(tmp2)
    
    inter = list((tmp1 & tmp2).elements())
    union = list((tmp1 | tmp2).elements())
    print(iter)
    print(union)
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    # if str1 == '' and str2 =='' 로 안되는 이유: 특수 기호때문에 arr1,2가 안 만들어지는 경우
    return int(len(inter)/len(union)*65536)