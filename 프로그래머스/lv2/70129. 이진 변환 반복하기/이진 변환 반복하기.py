def change(s): # int값인 s를 2진법으로 바꾼 뒤 string으로 return
    s_two = ''
    while s != 0:
        s_two = str(s % 2)+ s_two 
        s //= 2
    return s_two

def solution(s):
    # s에서 0을 제거하고, s의 길이를 2진법으로 표현
    # [s가 1이 될때까지의 2진법 변환 횟수, 제거된 0의 개수]
    change_cnt = 0
    cnt = 0
    
    while len(s) > 1:
        prev_len = len(s)
        s = [x for x in list(s) if x == "1"]
        cnt += prev_len - len(s)
        s = change(len(s))
        change_cnt += 1
    return [change_cnt, cnt]