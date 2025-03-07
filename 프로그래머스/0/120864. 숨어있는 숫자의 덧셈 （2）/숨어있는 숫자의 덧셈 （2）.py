def solution(my_string):
    answer = 0
    num="0"
    for i in my_string:
        if i.isdigit():
            num+=i
        else:
            answer+=int(num)
            num="0"
    
    answer+=int(num)
    
    return answer