def solution(N, stages):
    answer = []
    total_players = len(stages)
    from collections import Counter
    
    stage_counter = Counter(stages)

    for i in range(1, N + 1):
        if total_players == 0:
            failure = 0
        else:
            failure = stage_counter[i] / total_players
            total_players -= stage_counter[i]
        answer.append((i, failure))
    
    answer.sort(key=lambda x: x[1], reverse=True)
    
    return [x[0] for x in answer]
