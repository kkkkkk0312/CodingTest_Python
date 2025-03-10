def solution(my_string, is_suffix):
    a=[]
    for i in range(len(my_string)):
        a.append(my_string[i:])    
    if is_suffix in a:
        return 1
    else:
        return 0