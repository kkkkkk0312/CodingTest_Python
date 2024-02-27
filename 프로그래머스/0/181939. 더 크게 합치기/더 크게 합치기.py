def solution(a, b):
    result=lambda a,b: max(int(str(a) + str(b)), int(str(b) + str(a)))

    return result(a,b)