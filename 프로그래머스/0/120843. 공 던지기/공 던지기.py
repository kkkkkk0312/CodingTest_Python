def solution(numbers, k):

    answer=(k*2-1)%len(numbers)
    if answer==0:
        return len(numbers)
    else:
        return answer