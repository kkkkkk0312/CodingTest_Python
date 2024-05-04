from collections import Counter
def solution(strArr):
    answer = []
    for i in strArr:
        answer.append(len(i))
    a=Counter(answer)
    return max(a.values())