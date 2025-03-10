def solution(num_list, n):
    answer = []
    cnt=0
    row=[]
    for i in num_list: 
        row.append(i)
        cnt+=1
        if cnt==n:
            cnt=0
            answer.append(row)
            row=[]
    return answer