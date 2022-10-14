def solution(want, number, discount):
    #원하는 제품을 나타내는 문자열 배열 want
    #원하는 제품의 수량을 나타내는 정수 배열 number
    #XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount
    w_arr = dict()
    i = 0
    for item in want:
        w_arr[item] = number[i]
        i+=1
    
    days = 0
    # issue: discount, want의 개수가 다를 때 idx 처리
    for i in range(len(discount)-sum(number)+1):
        d_arr = dict()
        for j in range(i, i+sum(number)):
            if discount[j] in d_arr.keys(): #discount에 number의 key에 없을 수도 있음
                d_arr[discount[j]] += 1
            else:
                d_arr[discount[j]] = 1
        if d_arr == w_arr:
            days += 1
            
    return days