def solution(answers):
    cnt1=0
    cnt2=0
    cnt3=0
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    answer = []
    for i in range(len(answers)):
        if answers[i]==a1[i%5]:
            cnt1+=1
        if answers[i]==a2[i%8]:
            cnt2+=1
        if answers[i]==a3[i%10]:
            cnt3+=1
    max_num = max(cnt1, cnt2, cnt3)
    for idx, cnt in enumerate([cnt1, cnt2, cnt3], start=1):
        if cnt == max_num:
            answer.append(idx)
            
    return answer