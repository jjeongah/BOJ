def solution(s):
    arr = []
    for s in list(s):
        if s == "(":
            arr.append(s)
        elif s == ")":
            try:
                arr.pop()
            except:
                return False
    if arr == []:
        return True
    else:
        return False