from collections import Counter


def solution(k, tangerine):
    answer = 0

    for t, n in Counter(tangerine).most_common():
        if k > 0:
            k -= n
            answer += 1

    return answer