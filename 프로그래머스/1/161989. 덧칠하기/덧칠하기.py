def solution(n, m, section):
    answer = 0
    i = 0
    length = len(section)
    
    while i < length:
        answer += 1
        start = section[i]
        end = start + m - 1
        
        while i < length and section[i] <= end:
            i += 1
    
    return answer
