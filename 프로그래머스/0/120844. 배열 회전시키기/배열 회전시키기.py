def solution(numbers, direction):
    answer=[]
    if direction=='right':
        answer.append(numbers[-1])
        return answer+numbers[:-1]
    else:
        answer.append(numbers[0])
        return numbers[1:]+answer