def solution(s):
    cntp=0
    cnty=0
    for i in s:
        if i=='p' or i=='P':
            cntp+=1
        if i=='y' or i=='Y':
            cnty+=1
    if cntp==cnty:
        return True
    else:
        return False