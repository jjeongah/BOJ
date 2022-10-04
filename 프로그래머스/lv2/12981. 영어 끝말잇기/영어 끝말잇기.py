import math

def solution(n, words): # 먼저 탈락하는 사람의 번호, 몇 번째에 탈락하는 지 return
    # 탈락 이유: 1. 끝말 안 잇기 2. 단어 중복
    last = words[0][-1]
    for w in range(1, len(words)):
        if (words[w][0] != last) or (words[w] in words[:w]):
            return [w%n+1, w//n+1]
        last = words[w][-1]
    else:
        return [0,0]