def solution(arr, idx):
    answer = len(arr)
    for i in range(idx,len(arr)):
        if arr[i]==1:
            answer=i
            break
            
    if answer==len(arr):
        return -1
    else:
        return answer