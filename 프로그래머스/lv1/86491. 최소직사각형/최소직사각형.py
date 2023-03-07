'''
모든 명함을 수납할 수 있는 가장 작은 지갑
[a,b] 중 작은 애를 a, 큰 애를 b라고 정렬한 뒤 모든 a들 중 최대, 모든 b들 중 최대 값을 곱
'''
def solution(sizes):
    a, b= -1, -1
    for size in sizes:
        size.sort()
    for size in sizes:
        a = max(a, size[0])
        b = max(b, size[1])
    return a*b