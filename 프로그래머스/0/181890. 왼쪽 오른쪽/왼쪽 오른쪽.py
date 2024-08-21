def solution(str_list):
    for i,a in enumerate(str_list):
        if a=='l':
            return str_list[:i]
        elif a=='r':
            return str_list[i+1:]  
    
    return []