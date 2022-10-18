def solution(places):
    '''
    places: 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 
    p: 응시자가 앉아있는 자리, 0: 빈 테이블, x: 파티션
    
    각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return
    거리두기: 파티션이 없을 때 맨해튼 거리가 3~. 빈테이블이 있으면 안됨
    파티션이 있고 거리가 2여도 ok.
    
    idea: bfs도 가능할 것 같은데 빡구현도 가능할 것 같음
    '''
    answer = []
    for place in places: # 각 대기실별로 판별
        seats = [] # 참가자들의 row, col 정보
        for row in range(len(place)): 
            for col in range(len(place[0])):
                if place[row][col] == "P":
                    seats.append([row, col])
        
        # seats: [[0, 0], [0, 4], [2, 1], [2, 3], [4, 0], [4, 4]]
        # 거리두기 판별
        flag = 1 # flag가 0이면 거리두기를 지키지 않은 경우
        for i in range(len(seats)):
            for j in range(i+1, len(seats)):
                i_x, i_y = seats[i][0], seats[i][1]
                j_x, j_y = seats[j][0], seats[j][1]
                if abs(i_x-j_x) + abs(i_y-j_y) > 2: # 거리로 성공
                    continue
                
                # 거리로도 실패했는데 파티션으로도 실패
                if i_x == j_x and place[i_x][i_y+1] != 'X': # 행이나 열이 같을 때 파티션이 있는 경우
                    # tip! 어차피 거리 2일 때라 'X' in place[i_x][i_y:j_y] 할 필요 X
                    flag = 0
                    break
                if i_y == j_y and place[i_x+1][i_y] != 'X':
                    flag = 0
                    break
                if i_x != j_x and i_y != j_y and (place[i_x][j_y] != 'X' or place[j_x][i_y] != 'X'):
                    # 행이나 열이 다른데(대각선) 파티션이 있는 경우
                    flag = 0
                    break
        answer.append(flag)
        print('\n')
                
    return answer