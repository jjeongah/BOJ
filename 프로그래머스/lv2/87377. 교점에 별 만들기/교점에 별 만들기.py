def solution(line):
    '''
    line: 직선 Ax + By + C = 0 에 대한 정보가 담긴 배열 
    idea: 1. 교점 구하기 2. *로 print하기
    '''
    meet = [] # 교점의 좌표 담는 list
    for a,b,c in line:
        for d,e,f in line:
            if not (a==d and b==e and c==f) and (a*e != b*d): # 교점이 있는 경우
                x = (b*f-c*e) / (a*e-b*d) # 나누어 떨어져야 함
                y = (c*d-a*f) / (a*e-b*d)
                if (x == int(x) and y== int(y)) and [x,y] not in meet:
                    meet.append([int(x), int(y)]) # 나누면 float
                    
    x_min = min(meet)[0]
    x_max = max(meet)[0] # min(meet)[-1]
    y_min = min(meet, key = lambda x: x[1])[1]
    y_max = max(meet, key = lambda x: x[1])[1] #min(meet, key = lambda x: x[1])[-1]
    
    # 1. .으로 기본 좌표계(2차원 arr) 생성  2. *를 찍기
    coordinate = [['.']*(x_max-x_min+1) for _ in range(y_max - y_min+1)]
    for dot in meet:
        x, y = dot # 일반 좌표에서의 x,y 좌표
        new_x, new_y = abs(y_max -y), abs(x- x_min) 
        coordinate[new_x][new_y] = '*'
    
    answer = []
    for c in coordinate:
        answer.append(''.join(c))
    '''
    for i,v in enumerate(coordinate):
        star[i] = ''.join(v)
    '''
    return answer