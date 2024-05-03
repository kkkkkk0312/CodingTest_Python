def solution(numLog):
    answer = ''
    num=numLog[0]
    for i in numLog[1:]:
        if i-num==1:
            answer=answer+'w'
            num=i
        elif i-num==-1:
            answer=answer+'s'
            num=i
        elif i-num==10:
            answer=answer+'d'
            num=i
        else:
            answer=answer+'a'
            num=i
    return answer