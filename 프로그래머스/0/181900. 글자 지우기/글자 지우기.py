def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i in indices:
            continue
        answer=answer+my_string[i]    
    return answer