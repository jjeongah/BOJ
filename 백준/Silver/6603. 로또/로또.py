'''
1~49의 수 중 k개를 골라 집합 S를 만들고 그 수 내에서 6개 선택
return: 수를 고르는 방법들
'''
from itertools import combinations

while True:
    arr = list(map(int , input().split()))
    if arr == [0]:
        break
    #print(arr)
    combi_list = list(combinations(arr[1:], 6))
    for combi in combi_list:
        print(*combi)
    print()