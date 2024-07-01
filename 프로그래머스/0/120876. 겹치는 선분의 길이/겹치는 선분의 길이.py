def solution(lines):
    answer = 0
    box=[0]*200
    aa=[]
    for u in lines:
        p=[]
        for x in u:
            p.append(x+100)
        aa.append(p)    
        
    for i,j in aa:
        for k in range(i,j):
            box[k]=box[k]+1
    for q in box:
        if q>1:
            answer+=1
    return answer