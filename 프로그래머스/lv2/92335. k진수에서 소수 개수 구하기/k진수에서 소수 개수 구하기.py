def isPrime(n):
    if n == 1:
        return False
    for j in range(2, int(n**(1/2)+1)):
        if n % j == 0:
            return False
    return True
                   
def solution(n, k):
    # 10진수 n을 k진수로 바꿨을 때의 소수의 개수 return
    answer = 0
                   
    # 1. n을 k진수로 바꾸기
    new_n = ''
    while n>0:
        new_n = str(n % k)+new_n
        n //= k
    # 2. 0을 기준으로 나누고 소수 찾기
    n_list = new_n.split('0')
    for n in n_list:
        if n != '' and isPrime(int(n))==True:
              answer +=1         
    return answer