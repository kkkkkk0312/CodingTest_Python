def solution(my_string):
    a=['a','e','i','o','u']
    answer = ''
    for i in my_string:
        if i in a:
            continue
        answer=answer+i    
    return answer