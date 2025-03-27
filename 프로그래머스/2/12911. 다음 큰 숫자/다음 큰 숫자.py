def solution(n):
    answer = 0
    for i in range(n+1, n+1000000):
        if bin(i).count('1')==bin(n).count('1'):
            answer=i
            break
    return answer