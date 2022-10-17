from itertools import combinations
from functools import partial


def solution(relation):
    candidate_key = set()
    # 후보키가 될수 있는 조합 찾기
    # r: nCr 에서의 r
    col = len(relation[0])
    for r in range(1, col + 1):
        for case in combinations(range(col), r):
            issuperset = partial(set.issuperset, set(case))
            # (1) 최소성
            # 이미 확인된 후보키 중, 부분집합이 있나 확인->후보키중 하나라도 부분집합이 있으면, continue.
            if any(map(issuperset, candidate_key)):
                continue

            # (2) 유일성
            case_set = set([tuple(a[idx] for idx in case) for a in relation])
            if len(relation) == len(case_set):
                candidate_key.add(case)
                
    return len(candidate_key)