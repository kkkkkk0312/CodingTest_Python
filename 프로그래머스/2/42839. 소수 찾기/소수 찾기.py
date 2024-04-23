from itertools import permutations, combinations
import math
def solution(numbers):
    answer = []
    cnt=0
    for i in range(1,len(numbers)+1):
        num = permutations(numbers, i)
        for perm in num:
            answer.append(int(''.join(perm)))
    answer=set(answer) 
    if 0 in answer:
        answer.remove(0)
    if 1 in answer:
        answer.remove(1)
        print(answer)
    for a in answer:
        ddd=0
        for b in range(2,math.isqrt(a)+1):
            if a%b==0:
                ddd+=1
                break
        if ddd==0:
            cnt+=1        
    return cnt