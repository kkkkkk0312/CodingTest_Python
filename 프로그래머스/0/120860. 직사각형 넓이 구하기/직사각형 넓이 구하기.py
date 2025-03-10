import math
def solution(dots):
    max_x=dots[0][0]
    max_y=dots[0][1]
    min_x=dots[0][0]
    min_y=dots[0][1]
    for a,b in dots:
        if max_x<a:
            max_x=a
        if max_y<b:
            max_y=b
        if min_x>a:
            min_x=a
        if min_y>b:
            min_y=b
    return abs((max_x-min_x)*(max_y-min_y))