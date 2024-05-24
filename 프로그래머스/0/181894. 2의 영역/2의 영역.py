def solution(arr):
    answer = []
    for a,b in enumerate(arr):
        if b==2:
            answer.append(a)
    if len(answer)<=0:
        return [-1]
    else:
        return arr[answer[0]:answer[-1]+1]