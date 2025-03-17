def solution(n):
    a=1
    box=0
    answer=2
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for i in range(3,n+1):
            box=answer
            answer=answer+a
            a=box
        return answer%1234567
