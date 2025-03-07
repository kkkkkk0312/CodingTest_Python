def solution(array):
    num=0
    index=0
    for a,b in enumerate(array):
        if b>num:
            num=b
            index=a
    return [num, index]