from collections import Counter
def solution(k, tangerine):
    a=Counter(tangerine)
    aa = sorted(tangerine, key=lambda x: (a[x], x), reverse=True)
    return len(set(aa[:k]))