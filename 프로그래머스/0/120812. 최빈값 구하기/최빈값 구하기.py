def solution(array):
    cnt = 0
    a=[]
    for i in set(array):
        a.append(array.count(i))
        if cnt<array.count(i):
            cnt=array.count(i)
    
    for k in set(array):
        if cnt==array.count(k):
            cnt=k
            break
        
    a=sorted(a, reverse=True)
    if a.count(a[0])>=2:
        return -1
    else:
        return cnt