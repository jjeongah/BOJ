import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
arr = sorted(input().split()) # map을 사용한 string 변환 따로 할 필요 없음
answer = list(combinations(arr, L))
vowel = ['a', 'e', 'i', 'o', 'u']
for candidate in answer:
    vowel_cnt = 0
    not_vowel_cnt = 0
    for alphabet in candidate:
        if alphabet in vowel:
            vowel_cnt += 1
        else:
            not_vowel_cnt += 1
    if vowel_cnt > 0 and not_vowel_cnt > 1: # 최소 1개 모음, 2개 자음
        print(''.join(candidate))