def solution(lottos, win_nums):
    answer = []
    max_num=0
    min_num=0
    sum_num=lottos.count(0)
    a=[i for i in lottos if i!=0]
    for k in a:
        for j in win_nums:
            if k==j:
                min_num+=1
            
    max_num=min_num+sum_num    
    z={1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    
    answer.append(z.get(max_num, 6))
    answer.append(z.get(min_num, 6))
    return answer