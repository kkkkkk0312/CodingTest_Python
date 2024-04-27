def solution(arr, k):
    answer = []
    cnt=0
    for i in arr:
        if i not in answer:
            answer.append(i)
            cnt+=1
        if cnt==k:
            break
    
    if len(answer)<k:
        for a in range(k-len(answer)):
            answer.append(-1)
    return answer