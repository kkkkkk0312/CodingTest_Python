def solution(array, height):
    array.append(height)
    a=sorted(array, reverse=True)
    return a.index(height)