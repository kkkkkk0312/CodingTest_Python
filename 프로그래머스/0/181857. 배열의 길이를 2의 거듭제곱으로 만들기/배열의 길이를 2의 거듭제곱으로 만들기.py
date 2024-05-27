def solution(arr):
    answer = []
#     if len(arr)==1:
#         return arr
    
    for i in range(0,11):
        if len(arr)<2**i:
            for k in range((2**i)-len(arr)):
                arr.append(0)
        if len(arr) == 2**i:
            break
    return arr