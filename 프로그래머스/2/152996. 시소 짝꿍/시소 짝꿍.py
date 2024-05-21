import numpy as np
from collections import Counter
def solution(weights):
    cnt = 0
    tw = []
    
    for weight in weights:
        tw.append(weight * 2)
        tw.append(weight * 3 / 2)
        tw.append(weight * 4 / 3)
        
    count_og = Counter(weights)
    count_tw = Counter(tw)
    
    for weight in count_og:
        if count_og[weight] > 1:
            cnt += count_og[weight] * (count_og[weight] - 1) // 2
            
        if weight in count_tw:
            cnt += count_og[weight] * count_tw[weight]
            
    return cnt     