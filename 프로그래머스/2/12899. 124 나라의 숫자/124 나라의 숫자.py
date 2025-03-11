def solution(n):
    answer=''
    digits = ['1', '2', '4']  
    while n > 0:
        n -= 1  
        answer = digits[n % 3] + answer  
        n //= 3  

    return answer