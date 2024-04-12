def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex in i:
            continue
        answer=answer+i    
    return answer