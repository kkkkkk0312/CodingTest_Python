def solution(picture, k):
    answer = []
    
    for i in picture:
        row=[]
        for j in i:
            for num in range(k):
                row.append(j)
        
        a=''.join(row)
        
        for num in range(k):
            answer.append(a)
    return answer