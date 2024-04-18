def solution(array, commands):
    answer = []
    # aaa=array[commands[0][0]-1:commands[0][1]]
    # bbb=sorted(aaa,reverse=False)
    # ccc=bbb[commands[0][2]]
    for a,b,c in commands:
        aaa=array[a-1:b]
        bbb=sorted(aaa,reverse=False)
        ccc=bbb[c-1]
        answer.append(ccc)
        
    return answer