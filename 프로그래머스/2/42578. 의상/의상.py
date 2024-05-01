from itertools import combinations
from collections import defaultdict
def solution(clothes):
    
    clothes_dict = defaultdict(int)
    for name, type in clothes:
        clothes_dict[type] += 1
    
    answer=1   
    for type in clothes_dict:
        answer *= (clothes_dict[type] + 1)
        print(answer)
     

    return answer-1