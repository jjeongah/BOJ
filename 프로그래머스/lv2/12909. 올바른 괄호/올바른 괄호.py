def solution(s):
    arr = []
    for s in list(s):
        if s == "(":
            arr.append(s)
        elif s == ")":
            try:
                arr.pop()
                #pop(0)가 더 오래 걸림
            except:
                return False
    if arr == []:
        return True
    else:
        return False
