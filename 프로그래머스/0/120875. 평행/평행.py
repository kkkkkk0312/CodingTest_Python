def solution(dots):
    case1=(dots[1][0]-dots[0][0])/(dots[1][1]-dots[0][1])
    case2=(dots[3][0]-dots[2][0])/(dots[3][1]-dots[2][1])
    case3=(dots[2][0]-dots[0][0])/(dots[2][1]-dots[0][1])
    case4=(dots[3][0]-dots[1][0])/(dots[3][1]-dots[1][1])
    if case1==case2 or case3==case4:
        return 1
    else:
        return 0