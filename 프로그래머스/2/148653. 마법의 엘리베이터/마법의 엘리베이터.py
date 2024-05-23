def solution(storey):
    answer = 0
    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10  # 다음 자리 숫자 확인
        
        # 반올림 조건: 현재 숫자가 5보다 크거나, 5인데 다음 숫자가 5 이상인 경우
        if digit > 5 or (digit == 5 and next_digit >= 5):
            answer += 10 - digit  # 10에서 현재 숫자를 뺀 값을 더함
            storey = storey // 10 + 1  # 다음 자리 숫자를 1 증가시킴
        else:
            answer += digit  # 현재 숫자를 더함
            storey //= 10  # 다음 자리로 이동
        
    return answer