def solution(arr):
    answer = [[]]

    for i in arr:
        if len(arr)>len(i):
            for a in range(len(arr)-len(i)):
                i.append(0)
        elif len(arr)<len(i):
            for a in range(len(i)-len(arr)):
                arr.append([0,0,0,0])

    return arr