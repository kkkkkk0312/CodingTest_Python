def solution(myString):
    answer = ''
    for i in myString:
        if i<'l':
            i='l'
        answer=answer+i    
    return answer