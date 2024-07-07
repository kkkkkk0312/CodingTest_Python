import math
def solution(sides):
    answer = 0
    a=sorted(sides)
    for i in range(a[1]-a[0]+1,a[1]+1):
        answer+=1
    for j in range(a[1]+1,a[0]+a[1]):
        answer+=1
    return answer