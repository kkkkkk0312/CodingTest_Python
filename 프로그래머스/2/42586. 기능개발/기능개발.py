def solution(progresses, speeds):
    answer = []
    sample=[]
    num=0
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            sample.append((100-progresses[i])//speeds[i])
        else:
            sample.append(((100-progresses[i])//speeds[i])+1)
    print(sample)  
    ld=sample[0]
    for a in range(len(sample)):
        if sample[a]<=ld:
            num+=1
            continue
        else:
            answer.append(num)
            num=1
            ld=sample[a]
    answer.append(num)
    return answer