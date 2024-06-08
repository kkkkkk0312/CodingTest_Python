def solution(num, k):
    answer=-1
    a=list(str(num))
    for i,b in enumerate(a):
        if b==str(k):
            answer=i+1
            break
    return answer