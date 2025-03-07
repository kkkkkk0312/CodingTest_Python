def solution(A, B):
    answer = 0
    if A==B:
        return 0
    for i in range(1,len(A)+1):
        answer+=1
        print(A[-i:]+A[:-i])
        if (A[-i:]+A[:-i])==B:
            return answer
    return -1   
    