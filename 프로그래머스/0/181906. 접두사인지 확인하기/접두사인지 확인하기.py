def solution(my_string, is_prefix):
    a=[]
    aaa=''
    for i in my_string:
        aaa=aaa+i
        a.append(aaa)
        
    if is_prefix in a:
        return 1
    else:
        return 0
