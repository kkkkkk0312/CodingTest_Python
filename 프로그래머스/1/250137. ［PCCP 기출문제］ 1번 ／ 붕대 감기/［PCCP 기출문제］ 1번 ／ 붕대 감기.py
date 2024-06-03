def solution(bandage, health, attacks):
    answer = 0
    time=0
    a_stack=0
    hp=health
    b_stack=0
    for i in range(attacks[-1][0]+1):
        if time==attacks[a_stack][0]:
            hp=hp-attacks[a_stack][1]
            a_stack+=1
            b_stack=0
        else:
            if hp<health:
                hp=hp+bandage[1]
                b_stack+=1
                if hp>health:
                    hp=health
            if b_stack==bandage[0]:
                hp=hp+bandage[2]
                b_stack=0
                if hp>health:
                    hp=health
        time+=1
        if hp<=0:
            hp=-1
            break
        print(hp)    
        
    return hp