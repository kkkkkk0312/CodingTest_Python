def solution(my_string):
    answer = [0]*52
    ap='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in my_string:
        if i in ap:
            answer[ap.find(i)]+=1

    return answer