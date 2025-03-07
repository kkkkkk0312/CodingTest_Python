def solution(s):
    answer = ''
    index=0
    for a in s:
        if a==' ':
            answer+=" "
            index=0
            continue
        if index%2==0:
            answer+=a.upper()
            index+=1
        else:
            answer+=a.lower()
            index+=1
    return answer