def solution(chicken):
    cp = chicken  # 처음 받은 쿠폰 개수
    answer = 0  # 서비스 치킨 개수

    while cp >= 10:  # 쿠폰이 10장 이상이면 반복
        service = cp // 10  # 이번에 받을 수 있는 서비스 치킨
        answer += service  # 서비스 치킨 누적
        cp = cp % 10 + service  # 남은 쿠폰 + 새로 받은 쿠폰

    return answer

