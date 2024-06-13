def solution(my_string):
    answer = []
    a=0
    for i in my_string:
        try:
            a=int(i)
        except:
            continue
        answer.append(a)    
    return sorted(answer)