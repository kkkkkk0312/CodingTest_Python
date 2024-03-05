def solution(num_list):
    sum=0
    mul=1
    for i in num_list:
        sum=sum+i
        mul=mul*i
    if (sum*sum)>mul:
        return 1
    else:
        return 0