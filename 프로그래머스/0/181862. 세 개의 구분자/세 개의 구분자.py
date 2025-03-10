def solution(myStr):
    answer = []
    st=''
    for i in myStr:
        if i=='a' or i=='b' or i=='c':
            if st=='':
                continue
            answer.append(st)
            st=''
            continue
        else:
            st+=i
    answer.append(st)    
    
    if len(answer)==1 and answer[0]=="":
        return ["EMPTY"]
    else:
        return answer