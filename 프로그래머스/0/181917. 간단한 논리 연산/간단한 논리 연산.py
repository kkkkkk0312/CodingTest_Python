def solution(x1, x2, x3, x4):
    
    if x1==False and x2==False:
        a=False
    else:
        a=True
    if x3==False and x4==False:
        b=False
    else:
        b=True  
    if a==True and b==True:
        answer=True
    else:
        answer=False     
    return answer