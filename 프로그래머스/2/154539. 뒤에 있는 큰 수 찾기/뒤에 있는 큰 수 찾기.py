def solution(numbers):
    answer = [-1] * len(numbers)  # step 1
    stack = []  # step 2
    
    for i in range(len(numbers)):  # step 3
        while stack and numbers[stack[-1]] < numbers[i]:  # step 4
            index = stack.pop()  # step 5
            answer[index] = numbers[i]  # step 6
        stack.append(i)  # step 7    
           
    return answer