def solution(cipher, code):
    answer = ''
    for i,k in enumerate(cipher):
        if i%code==code-1:
            answer+=k
    return answer