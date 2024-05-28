def solution(s):
    answer = ''
    a=[int(x) for x in s.split()]
    answer=answer+str(min(a))+" "+str(max(a))
    return answer