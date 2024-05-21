from collections import deque
def solution(x, y, n):
    if x==y:
        return 0
    
    queue=deque([(x,0)])
    visited=set()
    visited.add(x)
    
    while queue:
        a,cnt=queue.popleft()
        operations=[a+n, a*2, a*3]
        
        for i in operations:
            if i==y:
                return cnt+1
            if i<y and i not in visited:
                visited.add(i)
                queue.append((i,cnt+1))
    
    return -1