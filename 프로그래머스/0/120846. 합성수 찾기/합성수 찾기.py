def solution(n):
    answer = 0
    for i in range(4,n+1):
        cnt=0
        for k in range(1,int(i**0.5)+1):
            if i%k==0:
                cnt+=2
            if cnt>=3:
                answer+=1
                break
                
    return answer