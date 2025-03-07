def solution(my_string, num1, num2):
    answer = ''
    a=[]
    for i in my_string:
        a.append(i)    
    box=[a[num1], a[num2]]
    for x,y in enumerate(a):
        if x==num1:
            answer+=box[1]
        elif x==num2:
            answer+=box[0]
        else:
            answer+=y
    return ''.join(answer)        
    