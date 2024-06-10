def solution(score):
    answer = []
    aa=[]
    for a,b in score:
        aa.append((a+b)/2)
    aa_s=sorted(aa) 
    aa_s.reverse()
    for i in aa:
        answer.append(aa_s.index(i)+1)
    return answer