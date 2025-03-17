def solution(n):
    answer = 1
    a=0
    box=0
    for i in range(1,n):
        box=answer
        answer=answer+a
        a=box
    return answer%1234567