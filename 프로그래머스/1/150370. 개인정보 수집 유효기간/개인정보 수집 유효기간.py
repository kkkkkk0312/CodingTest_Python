from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    
    today_date = datetime.strptime(today, '%Y.%m.%d')
    term_dict = {term.split()[0]: int(term.split()[1]) for term in terms}
    
    for idx, privacy in enumerate(privacies):
        date_str, term_type = privacy.rsplit(' ', 1)
        start_date = datetime.strptime(date_str, '%Y.%m.%d')
        
        months_to_add = term_dict[term_type]
        new_month = start_date.month + months_to_add
        new_year = start_date.year + (new_month - 1) // 12
        new_month = (new_month - 1) % 12 + 1
        
        # 만료일은 해당 월의 마지막 날로 설정
        new_day = start_date.day - 1
        if new_day == 0:
            new_month -= 1
            if new_month == 0:
                new_month = 12
                new_year -= 1
            new_day = 28
        
        expiration_date = datetime(new_year, new_month, new_day)
        
        # 만료일이 오늘 날짜 이전이면 answer에 추가
        if expiration_date < today_date:
            answer.append(idx + 1)
    
    return answer