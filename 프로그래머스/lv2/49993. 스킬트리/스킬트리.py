def solution(skill, skill_trees):
    '''
    skill: 선행 스킬 순서
    skill_trees: 유저가 만든 [유저가 스킬을 배울 순서]
    skill_trees에서 가능한 갯수 return
    '''
    cnt = 0
    for skills in skill_trees: #skills가 skill의 순서를 따르냐
    # 이전 요구 스킬을 모두 이전에 가지고 있어야 함
        flag = 1
        skill_idx = -1 # 실제 skill의 idx
        for s in skills:
            if s in skill:
                #print(s)
                skill_idx += 1
                if skill[skill_idx] != s:
                    flag = 0
        if flag == 1:
            cnt += 1
        print('\n')
        
    return cnt