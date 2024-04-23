def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    current_bridge_weight = 0
    elapsed_time = 0
    truck_index = 0
    
    while truck_index < len(truck_weights):
        # 1초가 지날 때마다 시간을 갱신
        elapsed_time += 1
        
        # 다리의 첫 번째 트럭이 다리를 다 건너면 무게에서 제거
        truck_left = bridge.pop(0)
        current_bridge_weight -= truck_left
        
        # 다음 트럭을 다리에 올릴 수 있는지 확인
        if current_bridge_weight + truck_weights[truck_index] <= weight:
            # 올릴 수 있으면 트럭을 추가하고 무게를 갱신
            bridge.append(truck_weights[truck_index])
            current_bridge_weight += truck_weights[truck_index]
            truck_index += 1
        else:
            # 올릴 수 없으면, 다리의 빈 공간을 추가하여 1초 지연
            bridge.append(0)
    
    # 마지막 트럭이 다리 위에 있는 시간을 추가
    elapsed_time += bridge_length
    
    return elapsed_time
    # answer = 0
    # a_list=[]
    # cnt=0
    # add=0    
    # i=0
    # while i<len(truck_weights):
    #     if add+truck_weights[i]<=weight:
    #         if len(a_list)>=bridge_length:
    #             a_list.pop() 
    #         add=add+truck_weights[i]
    #         a_list.insert(0,truck_weights[i])
    #         while len(a_list)<bridge_length:
    #             a_list.insert(0,0)
    #             cnt+=1
    #         i+=1
    #         cnt+=1
    #     else:
    #         if len(a_list)>=bridge_length:  
    #             add=add-a_list[-1]
    #             a_list.pop()     
    #             a_list.insert(0,0)
    #             cnt+=1
    # if bridge_length<len(truck_weights):
    #     return cnt
    # else:
    #     return cnt+1