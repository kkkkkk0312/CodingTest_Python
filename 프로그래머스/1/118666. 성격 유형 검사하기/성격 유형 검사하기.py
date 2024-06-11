def solution(survey, choices):
    a=[]
    answer = ''
    for i in range(len(survey)):
        if choices[i]==1:
            a.append(survey[i][:1])
            a.append(survey[i][:1])
            a.append(survey[i][:1])
        elif choices[i]==2:
            a.append(survey[i][:1])
            a.append(survey[i][:1])
        elif choices[i]==3:
            a.append(survey[i][:1])
        elif choices[i]==5:
            a.append(survey[i][1:])
        elif choices[i]==6:
            a.append(survey[i][1:])
            a.append(survey[i][1:])
        elif choices[i]==7:
            a.append(survey[i][1:])
            a.append(survey[i][1:])
            a.append(survey[i][1:])
    print(a)
    if a.count('R')<a.count('T'):
        answer+='T'
    else:
        answer+='R'
    if a.count('C')<a.count('F'):
        answer+='F'
    else:
        answer+='C'
    if a.count('J')<a.count('M'):
        answer+='M'
    else:
        answer+='J'
    if a.count('A')<a.count('N'):
        answer+='N'
    else:
        answer+='A'
       
    return answer