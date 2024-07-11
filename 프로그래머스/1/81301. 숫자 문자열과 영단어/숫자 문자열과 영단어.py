def solution(s):
    ss=''
    answer = ''
    a=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(s)):
        if s[i].isdigit()==True:
            answer=answer+str(s[i])
            continue
        else:
            ss=ss+s[i]
        for k in a:
            if ss==k:
                answer=answer+str(a.index(k))
                ss=''
    return int(answer)