def solution(num, total):
    answer = []
    aaa=0
    for i in range(0,num):
        aaa=i+aaa
    total=total-aaa
    x=total/num
    for _ in range(num):
        answer.append(x)
        x+=1
    return answer