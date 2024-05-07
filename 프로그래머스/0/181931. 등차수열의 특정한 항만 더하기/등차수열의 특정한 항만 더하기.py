def solution(a, d, included):
    answer = 0
    cnt=len(included)
    for i in range(cnt):
        if included[i]:
            answer=answer+(a+d*i)
    return answer