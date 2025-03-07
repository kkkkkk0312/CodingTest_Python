def solution(s):
    answer = 0
    index=[]
    a=s.split()
    for i,j in enumerate(a):
        if j=='Z':
            index.append(i-1)
            index.append(i)
    
    set_index=set(index)
    return sum(int(a[i]) for i in range(len(a)) if i not in set_index)