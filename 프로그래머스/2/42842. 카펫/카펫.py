def solution(brown, yellow):
    answer = []
    add=brown+yellow
    for i in range(1,int(add**(1/2))+1):
        if add%i==0:
            answer.append(i)
            if i < add//i:
                answer.append(add//i)
    answer.sort()    
    print(answer)
    real=[]
    for i in answer:
        if yellow==(i-2)*((add//i)-2):
            real.append([add/i,i])
    # if len(answer)%2==0:
    #     if yellow!=(answer[len(answer)//2]-2)*(answer[len(answer)//2-1]-2):
    #         real.append(answer[len(answer)//2+1])
    #         real.append(answer[len(answer)//2-2])
    #     else:    
    #         real.append(answer[len(answer)//2])
    #         real.append(answer[len(answer)//2-1])
    # else:
    #     real.append(answer[len(answer)//2])
    #     real.append(answer[len(answer)//2])
    return real[0]
