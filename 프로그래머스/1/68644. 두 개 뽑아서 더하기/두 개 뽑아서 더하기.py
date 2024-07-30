from itertools import combinations
def solution(numbers):
    answer=[]
    for i in combinations(numbers,2):
        if sum(i) in answer:
            continue
        answer.append(sum(i))
        
    return sorted(answer)