#키값 회전
def rotate(key):
    m = len(key)
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m - 1 - i] = key[i][j]
    return result

# 3. 키가 자물쇠에 맞는지 확인
def check(lock_padding):
    lock_length = len(lock_padding) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if lock_padding[i][j] != 1:
                return False
    return True

def solution(key, lock):
    '''
    key로 lock을 풀 수 있을까? => return true, false
    key의 일부분으로 lock을 풀 수 있는 경우도 고려해야함
    
    1. lock의 x,y축 길이가 3배로 padding을 준다
    2. key를 회전해가면서 움직인다
    3. lock가 전부 1로 채워진다면 정답으로 판별
    '''
    answer = False
    m, n = len(key), len(lock)
    
    lock_padding = [[0] * (n*3) for _ in range(n*3)] # 1. 새로운 잠금판 만들기
    for i in range(n):
        for j in range(n):
            lock_padding[i + n][j + n] = lock[i][j] # 중간을 원래 lock으로 채워줌
    
    # 2. key를 90도씩 4번 회전
    for k in range(4):
        n = len(lock_padding) // 3
        for x in range(n*2):
            for y in range(n*2):
                for i in range(len(key)):
                    for j in range(len(key)):
                        lock_padding[x + i][y + j] += key[i][j]
                if check(lock_padding) == True:
                    answer = True
                    return answer
                for i in range(len(key)):
                    for j in range(len(key)):
                        lock_padding[x + i][y + j] -= key[i][j]
        key = rotate(key)
    return answer