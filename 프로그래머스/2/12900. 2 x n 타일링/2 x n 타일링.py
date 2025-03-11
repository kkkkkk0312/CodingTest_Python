def solution(n):
    answer = [0]*(n+1)
    answer[0]=0
    answer[1]=1
    answer[2]=2
    for i in range(3,n+1): # i는 세로 타일의 수 
        answer[i]=((answer[i-1]+answer[i-2])%1000000007)
    return answer[-1]