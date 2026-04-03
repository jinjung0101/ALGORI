def day_calc(date_str):
    year, month, day = map(int, date_str.split('.'))
    return year * 12 * 28 + (month - 1) * 28 + (day - 1)


def solution(today, terms, privacies):
    answer = []
    today_calc = day_calc(today)

    terms_dic = {}
    for term in terms:
        kind, period = term.split()
        terms_dic[kind] = int(period)

    
    for idx, privacy in enumerate(privacies):
        date_str, kind = privacy.split()
        terms_calc = (terms_dic[kind] * 28) - 1 
        if day_calc(date_str) + terms_calc < today_calc:
            answer.append(idx + 1)
            
    return answer