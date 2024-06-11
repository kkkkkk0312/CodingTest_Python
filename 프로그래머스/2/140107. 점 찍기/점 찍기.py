import math

def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        max_j = math.floor(math.sqrt(d * d - i * i))
        answer += (max_j // k) + 1
    return answer