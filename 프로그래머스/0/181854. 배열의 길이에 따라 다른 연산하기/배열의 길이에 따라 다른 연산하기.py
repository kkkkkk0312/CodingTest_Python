def solution(arr, n):
    answer = []
    if len(arr)%2==1:
        for i,j in enumerate(arr):
            if i%2==0:
                j=j+n
                answer.append(j)
            else:
                answer.append(j)
    else:
        for i,j in enumerate(arr):
            if i%2==1:
                j=j+n
                answer.append(j)
            else:
                answer.append(j)

    return answer