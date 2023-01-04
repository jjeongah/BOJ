'''
한 번에 한 명 신고 가능. 여러 번 신고해도 한 번으로 처리
k번 이상 신고된 유저는 정지

id_list: 이용자의 id
report: 각 이용자가 신고한 이용자 *중복 제거* (a b : a가 b를 신고했다)
k: 정지 기준

각 유저별로 처리 결과 메일을 받은 횟수(신고한 사람 중 몇 명이 정지됨?)
'''
from collections import defaultdict

def solution(id_list, report, k):
    answer = [0]*(len(id_list))

    num = defaultdict(int) # num[x] = y : x가 y번 신고를 당했다
    people = defaultdict(set) # people[x] = [y1, y2] : x를 신고한 사람은 y1,y2 
    report = set(report)
    
    for r in report:
        a, b = r.split(' ') # a(신고자)가 b(신고당한사람)를 신고했다
        num[b] += 1
        people[b].add(a)
    
    #print(num)
    #print(people)
    
    for i in id_list: # i는 신고 당한 사람
        if i not in num: # 한 번도 신고 안 당한 경우
            continue
        if num[i] >= k:
            for j in people[i]:
                a = id_list.index(j)
                #print(b, id_list[a])
                answer[a] += 1
    
    return answer