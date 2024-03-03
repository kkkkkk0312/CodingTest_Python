def solution(num_list):
    a=''
    b=''
    for i in num_list:
        if i%2==1:
            a=a+str(i)
        else:
            b=b+str(i)
    return int(a)+int(b)